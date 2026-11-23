# KH Reference Integrity

**Open-source Academic Reference & Citation Validator**  
Prepared by **Khaled Hammadi** — Digital Media, Artificial Intelligence & Academic Research.

[العربية](#العربية) | [English](#english)

## العربية

أداة مفتوحة المصدر لفحص أولي لقوائم المراجع الأكاديمية. تساعد على اكتشاف النواقص الشكلية، والتكرارات المحتملة، وصيغ DOI غير السليمة بنيوياً.

> **حدود مهمة:** لا تثبت هذه الأداة أن مرجعاً ما موجود فعلاً، ولا تؤكد صحة بياناته أو صحة الاستشهاد داخل متن البحث. فحص DOI في هذا الإصدار شكلي فقط، وليس استعلاماً إلى Crossref أو DataCite.

### المتطلبات
- Python 3.10 أو أحدث
- لا تحتاج إلى مكتبات خارجية

### التشغيل
```bash
python -m kh_reference_integrity references.txt
python -m kh_reference_integrity references.txt --format json --output report.json
```

يمكنك أيضاً تشغيل الاختبارات:
```bash
python -m unittest discover -s tests -v
```

### مثال
ضع كل مرجع في سطر مستقل داخل `references.txt`، ثم شغّل الأمر أعلاه. سيعرض التقرير:
- الحقول التي أمكن استنتاجها مبدئياً.
- عناصر البيانات التي تبدو ناقصة.
- DOI إن وُجد، مع فحص شكلي لبنيته.
- التكرارات المحتملة.
- درجة اكتمال شكلية، وليست درجة موثوقية علمية.

### خارطة الطريق
راجع [ROADMAP.md](ROADMAP.md).

## English

A lightweight, dependency-free first-pass checker for academic reference lists. It flags likely missing fields, possible duplicates, and malformed DOI strings.

**Important limitation:** this release does not verify that a work exists, validate metadata against a registry, or check in-text citation/reference-list consistency. DOI checks are syntactic only.

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.
