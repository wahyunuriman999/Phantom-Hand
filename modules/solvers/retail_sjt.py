"""
Phantom-Hand: Situational Judgement Test (SJT) Solver for Retail & Merchandising
Formalizes organizational decision matrices for Head Office and Store Operations
(Merchandising Support, Frontline Sales, Stakeholder Alignment, and Compliance).
"""

from typing import Dict, Any, List


class RetailSJTSolver:
    """
    Situational Judgement Test decision matrix for retail corporate cases.
    """

    # Verified Decision Keys for Merchandising Support Officer (6 Cases)
    MERCHANDISING_SUPPORT_KEYS: Dict[int, Dict[str, Any]] = {
        1: {
            "best_option_idx": 3,
            "title": "Data Rekap Stok 200 Toko",
            "competency": "Continuous Improvement & Team Collaboration",
            "text": "Mencoba menyusun cara pengolahan yang lebih ringkas, lalu menawarkan ke tim apakah cara ini juga bisa dipakai."
        },
        2: {
            "best_option_idx": 3,
            "title": "Ketergantungan Jawaban pada Senior",
            "competency": "Self-Directed Learning & Autonomy",
            "text": "Meluangkan waktu di sela pekerjaan untuk menelusuri SOP dan data sebelumnya agar pemahaman Anda lebih menyeluruh."
        },
        3: {
            "best_option_idx": 3,
            "title": "Revisi Stok Artikel Utama Dekat Cut-Off",
            "competency": "Risk Management & Safe Prioritization",
            "text": "Menyampaikan temuan risiko kepada atasan dan melanjutkan pekerjaan dengan pengaturan prioritas yang lebih aman."
        },
        4: {
            "best_option_idx": 1,
            "title": "Selisih Stok Signifikan vs Momentum Promosi",
            "competency": "Stakeholder Consensus & Risk Alignment",
            "text": "Menyampaikan bahwa terdapat perbedaan data, lalu meminta kesepakatan bersama tentang bagaimana data tersebut digunakan untuk keputusan saat ini."
        },
        5: {
            "best_option_idx": 0,
            "title": "Konflik Sumber Data Lapangan vs Pusat vs IT",
            "competency": "Analytical Synthesis & Stakeholder Facilitation",
            "text": "Mengelompokkan perbedaan data yang ada, menyepakati penggunaan data untuk kebutuhan saat ini, lalu merangkum implikasinya secara singkat."
        },
        6: {
            "best_option_idx": 3,
            "title": "Usul Senior Memanipulasi Angka Penjualan",
            "competency": "Uncompromising Integrity & Strategic Insight",
            "text": "Menyusun laporan dengan angka aktual, namun menambahkan konteks penjelasan agar penurunan bisa dipahami dan memberikan insight perbaikan."
        }
    }

    # Verified Decision Keys for Store Sales Officer (8 Cases)
    SALES_OFFICER_KEYS: Dict[int, Dict[str, Any]] = {
        1: {
            "best_option_idx": 0,
            "title": "Penjualan Stagnan & Pelanggan Sering Tanya Fitur",
            "competency": "Proactive Consultative Selling",
            "text": "Mendiskusikan dengan supervisor kemungkinan membuat alat bantu sederhana (misalnya ringkasan perbandingan fitur) yang tetap sesuai kebijakan toko."
        },
        2: {
            "best_option_idx": 3,
            "title": "Kurang Meyakinkan Menghadapi Kompetitor Baru",
            "competency": "Lost Sales Reflection & Peer Mentoring",
            "text": "Mengamati kembali percakapan dengan pelanggan yang tidak jadi membeli, lalu mendiskusikannya dengan rekan yang lebih berpengalaman saat ada waktu."
        },
        3: {
            "best_option_idx": 1,
            "title": "Debat Rekan Kerja Soal Tugas Shift & Stok",
            "competency": "Operational Continuity & Pragmatic Escalation",
            "text": "Mengingatkan bahwa pembagian tugas sudah mengikuti jadwal yang ditetapkan dan meminta mereka menyelesaikan shift terlebih dahulu, lalu menyarankan agar perbedaan pendapat disampaikan kepada supervisor nanti."
        },
        4: {
            "best_option_idx": 2,
            "title": "Target Pribadi Tercapai & Peluang Repeat Order",
            "competency": "Team Enablement & Store Target Ownership",
            "text": "Melakukan pendekatan aktif kepada pelanggan repeat order dan membagikan pengalaman atau cara follow-up yang efektif kepada rekan tim."
        },
        5: {
            "best_option_idx": 2,
            "title": "Keterlambatan Pengiriman Barang & Komplain Pelanggan",
            "competency": "High Accountability & Corrective Action",
            "text": "Mengakui bahwa Anda belum memastikan proses koordinasi berjalan optimal, menjelaskan faktor penyebab, dan menyampaikan rencana perbaikan agar kejadian serupa tidak terulang"
        },
        6: {
            "best_option_idx": 0,
            "title": "Rekan Minta Pinjam Uang Petty Cash Toko",
            "competency": "Strict Financial Compliance with Empathetic Escalation",
            "text": "Menyarankan rekan untuk mengajukan bantuan resmi melalui Store Manager atau HR, meskipun prosesnya mungkin lebih lama dan belum tentu disetujui tepat waktu."
        },
        7: {
            "best_option_idx": 0,
            "title": "Barang Mahal Cacat Fisik vs Shrinkage Bulanan",
            "competency": "Procedural Compliance & Honesty",
            "text": "Melaporkan kondisi barang sesuai prosedur sebagai barang rusak dan mengikuti alur penanganan yang berlaku."
        },
        8: {
            "best_option_idx": 2,
            "title": "Beda Ide Tata Letak Display Pintu Masuk",
            "competency": "Collaborative Co-Creation & Sinergy",
            "text": "Mendengarkan argumen rekan, menggali kelebihan tiap ide bersama-sama, lalu mengajak rekan tersebut merancang solusi gabungan yang mengoptimalkan kedua ide."
        }
    }

    @classmethod
    def get_merchandising_action(cls, question_num: int) -> Dict[str, Any]:
        return cls.MERCHANDISING_SUPPORT_KEYS.get(question_num, {})

    @classmethod
    def get_sales_action(cls, question_num: int) -> Dict[str, Any]:
        return cls.SALES_OFFICER_KEYS.get(question_num, {})
