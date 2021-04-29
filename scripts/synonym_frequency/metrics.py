from scipy import spatial
import numpy as np
import pickle

def getPrimaryPercent(transFreqDict, translatedCountsOnly = False):
  primaryCount = 0
  totalCount = 0
  for word, info in transFreqDict.items():
    if len(info['translations']) < 1:
      continue
    
    primaryCount += info['translations'][0][1]
    curTotalCount = 0
    if translatedCountsOnly:
      for translationFrequency in info['translations']:
        curTotalCount += translationFrequency[1]
      totalCount += curTotalCount
    else:
      totalCount += info['count']

  return primaryCount / totalCount

def getSynonymTTR(transFreqDict):
  counted = 0
  numTypes = 0
  numTokens = 0
  totalUnweightedTTR = 0.0
  for word, info in transFreqDict.items():
    if len(info['translations']) < 1:
      continue
    
    curNumTokens = 0
    curNumTypes = 0
    for translationFrequency in info['translations']:
      curNumTokens += translationFrequency[1]
      if translationFrequency[1] > 0:
        curNumTypes += 1

    if curNumTokens > 0:
      counted += 1
      totalUnweightedTTR += (curNumTypes / curNumTokens) 
      numTokens += curNumTokens
      numTypes += curNumTypes

  return numTypes / numTokens, totalUnweightedTTR / counted

def getDifferenceFromUniform(transFreqDict):
  counted = 0
  totalDistance = 0
  for word, info in transFreqDict.items():
    if len(info['translations']) < 2:
      continue
    
    counted += 1
    transFreqs = []
    for translationFrequency in info['translations']:
      transFreqs.append(translationFrequency[1])
    transCount = sum(transFreqs)
    if transCount > 0:
      transFreqs = np.array(transFreqs) / transCount
      uniformFreqs = np.ones(len(info['translations']))
      distance = spatial.distance.cosine(uniformFreqs, transFreqs)
      totalDistance += distance
    else:
      totalDistance += 1.0
      
  return totalDistance / counted

with open('transFreqDictRef.pkl', 'rb') as infile:
  transFreqDictRef = pickle.load(infile)
with open('transFreqDictTrans.pkl', 'rb') as infile:
  transFreqDictTrans = pickle.load(infile)
with open('transFreqDictLSTM.pkl', 'rb') as infile:
  transFreqDictLSTM = pickle.load(infile)
with open('transFreqDictSMT.pkl', 'rb') as infile:
  transFreqDictSMT = pickle.load(infile)
with open('transFreqDictRBMTNoErr.pkl', 'rb') as infile:
  transFreqDictRBMTNoErr = pickle.load(infile)
with open('transFreqDictRBMTOnl.pkl', 'rb') as infile:
  transFreqDictRBMTOnl = pickle.load(infile)


print('Compute type token ratio for synoynms only, weighted and unweighted')

synonymTTRRef, unweightedSynonymTTRRef = getSynonymTTR(transFreqDictRef)
synonymTTRTrans, unweightedSynonymTTRTrans = getSynonymTTR(transFreqDictTrans)
synonymTTRLSTM, unweightedSynonymTTRLSTM = getSynonymTTR(transFreqDictLSTM)
synonymTTRSMT, unweightedSynonymTTRSMT = getSynonymTTR(transFreqDictSMT)
synonymTTRRBMTNoErr, unweightedSynonymTTRRBMTNoErr = getSynonymTTR(transFreqDictRBMTNoErr)
synonymTTRRBMTOnl, unweightedSynonymTTRRBMTOnl = getSynonymTTR(transFreqDictRBMTOnl)

print(synonymTTRRef, unweightedSynonymTTRRef)
print(synonymTTRTrans, unweightedSynonymTTRTrans)
print(synonymTTRLSTM, unweightedSynonymTTRLSTM)
print(synonymTTRSMT, unweightedSynonymTTRSMT)
print(synonymTTRRBMTNoErr, unweightedSynonymTTRRBMTNoErr)
print(synonymTTRRBMTOnl, unweightedSynonymTTRRBMTOnl)

print('Cosine difference between uniform and actual synoynm distribution')

uniformDistanceRef = getDifferenceFromUniform(transFreqDictRef)
uniformDistanceTrans = getDifferenceFromUniform(transFreqDictTrans)
uniformDistanceLSTM = getDifferenceFromUniform(transFreqDictLSTM)
uniformDistanceSMT = getDifferenceFromUniform(transFreqDictSMT)
uniformDistanceRBMTNoErr = getDifferenceFromUniform(transFreqDictRBMTNoErr)
uniformDistanceRBMTOnl = getDifferenceFromUniform(transFreqDictRBMTOnl)

print(uniformDistanceRef)
print(uniformDistanceTrans)
print(uniformDistanceLSTM)
print(uniformDistanceSMT)
print(uniformDistanceRBMTNoErr)
print(uniformDistanceRBMTOnl)

print('Percentage a token was translated to primary word/phrase, only counting if translation identified')
primaryPercentRef = getPrimaryPercent(transFreqDictRef, True)
primaryPercentTrans = getPrimaryPercent(transFreqDictTrans, True)
primaryPercentLSTM = getPrimaryPercent(transFreqDictLSTM, True)
primaryPercentSMT = getPrimaryPercent(transFreqDictSMT, True)
primaryPercentRBMTNoErr = getPrimaryPercent(transFreqDictRBMTNoErr, True)
primaryPercentRBMTOnl = getPrimaryPercent(transFreqDictRBMTOnl, True)

print(primaryPercentRef)
print(primaryPercentTrans)
print(primaryPercentLSTM)
print(primaryPercentSMT)
print(primaryPercentRBMTNoErr)
print(primaryPercentRBMTOnl)
