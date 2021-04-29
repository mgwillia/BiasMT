To reproduce our synonym frequency results, you need to do the following.

1. Ensure data (`out.tok` files) can be found under a directory `data`, which must be located at the same directory as these scripts
2. Acquire a token for `https://www.dictionaryapi.com/api` if using Spanish, and insert in the appropriate place in `english_to_spanish_translate.py`. The dictionary for English-French is included (`eng-fra.xml`) in this directory. Source is credited and can be found in the `.xml` file itself.
3. Download spacy language models
   ```
   python -m spacy download en
   python -m spacy download es
   python -m spacy download fr
   ```
4. Run `preprocess-[src]-[tgt].py`
5. If using `en-fr`, run `generate-pos-dict.py`
6. Run `calculate-synonym-frequency-[src]-[tgt].py`
7. Run `metrics.py`


For questions or concerns, please reach out: `mgwillia@umd.edu`
