import json
import pickle

posDict = {}

def addToPosDict(targetSentences, targetPOS):
    for idx, sentence in enumerate(targetSentences):
        currentPOS = targetPOS[idx]
        for wordIdx, word in enumerate(sentence):
            pos = currentPOS[wordIdx]
            if word not in posDict:
                posDict[word] = []
            if pos not in posDict[word]:
                posDict[word].append(pos)

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

addToPosDict(tgtLemSentsRef, tgtPOSRef)
addToPosDict(tgtLemSentsTrans, tgtPOSTrans)
addToPosDict(tgtLemSentsLSTM, tgtPOSLSTM)
addToPosDict(tgtLemSentsSMT, tgtPOSSMT)
addToPosDict(tgtLemSentsRBMTNoErr, tgtPOSRBMTNoErr)
addToPosDict(tgtLemSentsRBMTOnl, tgtPOSRBMTOnl)

with open('posDict.json', 'w') as jsonFile:
    json.dump(posDict, jsonFile)
