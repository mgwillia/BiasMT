import pickle
import operator
from english_to_spanish_translate import EnglishSpanishTranslator

NUM_WORDS = 1000
englishSpanishTranslator = EnglishSpanishTranslator()

def getSynonymFrequencyDictsUsingDictionary(sourceLemmaFreqDictSorted, sourceLemmatizedSentences, sourcePOS, targetLemmatizedSentences, targetPOS, numSourceWordsToAnalyze):
  lines = []
  backupDict = {}
  transFreqDict = {}
  for word, count in sourceLemmaFreqDictSorted[:numSourceWordsToAnalyze]:
    if word in ['apos', 'will', 'would']:
      continue

    trans_freq = {}
    for idx, targetSentence in enumerate(targetLemmatizedSentences):

      es_trans = []
      wordIndexes = [i for i, w in enumerate(sourceLemmatizedSentences[idx]) if w == word]
      for wordIndex in wordIndexes:
        pos = sourcePOS[idx][wordIndex]
        es_trans.extend(englishSpanishTranslator.getSpanishTranslationsFromDict(word, pos))

      if len(wordIndexes) > 0:
        if len(es_trans) == 0:
          if word not in backupDict:
            try:
              backupDict[word] = englishSpanishTranslator.getSpanishTranslations(word)
            except:
              backupDict[word] = list(set([]))
          es_trans = backupDict[word]
        for trans in es_trans:
          trans = trans.strip()
          if trans not in trans_freq:
            trans_freq[trans] = 0
          if ' ' not in trans:
            transIndexes = [i for i, t in enumerate(targetSentence) if t == trans]
            trans_freq[trans] += len(transIndexes)
            for transIndex in transIndexes:
              if targetPOS[idx][transIndex] == pos:
                trans_freq[trans] += 1
          else:
            for i, lemma in enumerate(targetSentence):
              transWordSplitList = trans.split(' ')
              j = 0
              while j < len(transWordSplitList) and transWordSplitList[j] == targetSentence[i + j]:
                j += 1
              if j == len(transWordSplitList):
                trans_freq[trans] += 1
                for otherTrans in es_trans:
                  if otherTrans.strip() in trans and otherTrans.strip() != trans:
                    if otherTrans.strip() not in trans_freq:
                      trans_freq[otherTrans.strip()] = 0
                    trans_freq[otherTrans.strip()] -= 1
        print(sourceLemmatizedSentences[idx])
        print(targetSentence)
        print(trans_freq)
        print('\n')
              
    trans_freq_sorted = sorted(trans_freq.items(), key=operator.itemgetter(1), reverse=True)
    print(word, count)
    print(trans_freq_sorted)
    transFreqDict[word] = {
        'count': count,
        'translations': trans_freq_sorted
    }
    line = 'Word: ' + word + ', Count: ' + str(count) + ', (Translation, Count): ' + str(trans_freq_sorted)
    lines.append(line)
    
  with open('translation_synonym_counts_v0.txt', 'w') as write_file:
    for line in lines:
      write_file.write(line + '\n')
    
  return transFreqDict

with open('sourceLemmaFreqDictSorted.pkl', 'rb') as infile:
  srcLemFreqDictSort = pickle.load(infile)
with open('sourceLemmatizedSentences.pkl', 'rb') as infile:
  srcLemSents = pickle.load(infile)
with open('sourcePartsOfSpeech.pkl', 'rb') as infile:
  sourcePOS = pickle.load(infile)

with open('targetLemmatizedSentencesRef.pkl', 'rb') as infile:
    tgtLemSentsRef = pickle.load(infile)
with open('targetLemmatizedSentencesTrans.pkl', 'rb') as infile:
    tgtLemSentsTrans = pickle.load(infile)
with open('targetLemmatizedSentencesLSTM.pkl', 'rb') as infile:
    tgtLemSentsLSTM = pickle.load(infile)
with open('targetLemmatizedSentencesSMT.pkl', 'rb') as infile:
    tgtLemSentsSMT = pickle.load(infile)
with open('targetLemmatizedSentencesRBMTNoErr.pkl', 'rb') as infile:
    tgtLemSentsRBMTNoErr = pickle.load(infile)
with open('targetLemmatizedSentencesRBMTOnl.pkl', 'rb') as infile:
    tgtLemSentsRBMTOnl = pickle.load(infile)

with open('targetPartsOfSpeechRef.pkl', 'rb') as infile:
    tgtPOSRef = pickle.load(infile)    
with open('targetPartsOfSpeechTrans.pkl', 'rb') as infile:
    tgtPOSTrans = pickle.load(infile)
with open('targetPartsOfSpeechLSTM.pkl', 'rb') as infile:
    tgtPOSLSTM = pickle.load(infile)
with open('targetPartsOfSpeechSMT.pkl', 'rb') as infile:
    tgtPOSSMT = pickle.load(infile)
with open('targetPartsOfSpeechRBMTNoErr.pkl', 'rb') as infile:
    tgtPOSRBMTNoErr = pickle.load(infile)
with open('targetPartsOfSpeechRBMTOnl.pkl', 'rb') as infile:
    tgtPOSRBMTOnl = pickle.load(infile)

transFreqDictRef = getSynonymFrequencyDictsUsingDictionary(srcLemFreqDictSort, srcLemSents, sourcePOS, tgtLemSentsRef, tgtPOSRef, NUM_WORDS)
transFreqDictTrans = getSynonymFrequencyDictsUsingDictionary(srcLemFreqDictSort, srcLemSents, sourcePOS, tgtLemSentsTrans, tgtPOSTrans, NUM_WORDS)
transFreqDictLSTM = getSynonymFrequencyDictsUsingDictionary(srcLemFreqDictSort, srcLemSents, sourcePOS, tgtLemSentsLSTM, tgtPOSLSTM, NUM_WORDS)
transFreqDictSMT = getSynonymFrequencyDictsUsingDictionary(srcLemFreqDictSort, srcLemSents, sourcePOS, tgtLemSentsSMT, tgtPOSSMT, NUM_WORDS)
transFreqDictRBMTNoErr = getSynonymFrequencyDictsUsingDictionary(srcLemFreqDictSort, srcLemSents, sourcePOS, tgtLemSentsRBMTNoErr, tgtPOSRBMTNoErr, NUM_WORDS)
transFreqDictRBMTOnl = getSynonymFrequencyDictsUsingDictionary(srcLemFreqDictSort, srcLemSents, sourcePOS, tgtLemSentsRBMTOnl, tgtPOSRBMTOnl, NUM_WORDS)

with open('transFreqDictRef.pkl', 'wb') as output:
  pickle.dump(transFreqDictRef, output)
with open('transFreqDictTrans.pkl', 'wb') as output:
  pickle.dump(transFreqDictTrans, output)
with open('transFreqDictLSTM.pkl', 'wb') as output:
  pickle.dump(transFreqDictLSTM, output)
with open('transFreqDictSMT.pkl', 'wb') as output:
  pickle.dump(transFreqDictSMT, output)
with open('transFreqDictRBMTNoErr.pkl', 'wb') as output:
  pickle.dump(transFreqDictRBMTNoErr, output)
with open('transFreqDictRBMTOnl.pkl', 'wb') as output:
  pickle.dump(transFreqDictRBMTOnl, output)
