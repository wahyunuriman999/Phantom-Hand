"""
Phantom-Hand Example: Automated Assessment Protocol with Human-in-the-Loop Safe Exit
Demonstrates how to answer N-1 questions in a portal and safely leave the final item for human verification.
"""

import time
import json
from modules.browser_sniper import BrowserSniper
from modules.solvers.competency_profiler import CompetencyProfiler


def run_assessment_workflow(target_window_title="Assessment Center", total_items=18):
    print(f"[*] Targeting window: {target_window_title}")
    
    # 1. Scrape questions from DOM
    print("[*] Scraping question panels...")
    scrape_js = """function() {
        var panels = $('.test-wrapper .panel.panel-test');
        var data = [];
        panels.each(function(idx, el) {
            data.push({
                num: idx + 1,
                text: $(el).find('.question-content').text().trim()
            });
        });
        return data;
    }"""
    
    questions = BrowserSniper.eval_js(target_window_title, scrape_js)
    if not isinstance(questions, list):
        print("[-] Failed to scrape questions or window not found:", questions)
        return

    print(f"[+] Successfully extracted {len(questions)} items from DOM.")

    # 2. Build optimal Likert profile (safely excluding the last item)
    profile = CompetencyProfiler.build_profile(questions, exclude_last=True)

    # 3. Create pacing action sequence
    items_to_answer = [p for p in profile.values() if not p["leave_for_user"]]
    print(f"[*] Generating batch injection for {len(items_to_answer)} items...")

    answers_map = {item["question_num"]: item["recommended_score"] for item in items_to_answer}
    answers_json = json.dumps(answers_map)

    batch_js = f"""(function(){{
        var ansMap = {answers_json};
        var panels = $('.test-wrapper .panel.panel-test');
        var keys = Object.keys(ansMap);
        var idx = 0;
        
        function step() {{
            if (idx >= keys.length) {{
                // Navigate view to the final question for the user
                if (typeof SetSlick === 'function') {{
                    SetSlick('goto', {total_items - 1});
                }}
                return;
            }}
            var qNum = parseInt(keys[idx]);
            var targetScore = ansMap[qNum].toString();
            var $p = panels.eq(qNum - 1);
            var $tr = $p.find('tr[data-test-trigger="multiplechoice"]').filter(function(){{
                var txt = $(this).text().trim();
                return txt.indexOf(targetScore + ' :') !== -1 || txt.startsWith(targetScore);
            }});
            
            if ($tr.length > 0) {{
                $tr.click();
            }}
            idx++;
            setTimeout(step, 350);
        }}
        step();
    }})();"""

    BrowserSniper.inject_js(target_window_title, batch_js)
    print(f"[+] Injected batch answers. Active viewport transitioned to Question {total_items}.")
    print(f"[!] Human-in-the-Loop Safeguard: Question {total_items} was intentionally left for manual review.")


if __name__ == "__main__":
    run_assessment_workflow()
