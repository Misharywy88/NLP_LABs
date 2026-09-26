# SMS Spam Collection

- Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)
- Download: https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip
- Retrieved: 2026-09-27
- Creators: Tiago Almeida and Jose Maria Gomez Hidalgo.
- Citation: Almeida, T. & Hidalgo, J. (2011). *SMS Spam Collection* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5CC84
- License listed by UCI: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

## Format and preservation

`SMSSpamCollection.txt` is the original archive member `SMSSpamCollection`, renamed to add a file extension. Its bytes have not been changed. The authors' `readme` is included unchanged as `SOURCE_README.txt`.

Each line contains a label, a tab, and a message. There is no header. `ham` means a normal message; `spam` means an unsolicited message. The notebook assigns column names `label` and `message`.

The included download has 5,574 rows: 4,827 ham and 747 spam. Counts in the notebook are computed from this file, not from another repackaged version. Duplicate rows are retained.

SHA-256 of `SMSSpamCollection.txt`:

```text
7d039a24a6083ed9ef0f806ebad56bbb976e3aeb8de05669173bfdc4996c239d
```
