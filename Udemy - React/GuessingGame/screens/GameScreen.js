import { View, StyleSheet, Text, FlatList } from 'react-native'
import Title from '../components/ui/Title'
import { useState, useEffect } from 'react'
import NumberContainer from '../components/game/NumberContainer'
import PrimaryButton from '../components/ui/PrimaryButton'
import Card from '../components/ui/Card'
import InstructionText from '../components/ui/InstructionsText'
import { Ionicons } from '@expo/vector-icons'
import GuessLogItem from '../components/game/GuessLogItem'

function generateRandomNumberBetween(min, max, exclude = 0) {
  const rndNum = Math.floor(Math.random() * (max - min) + min)
  if (rndNum == exclude) {
    return generateRandomNumberBetween(min, max, exclude)
  } else {
    return rndNum
  }
}

let minBoundary
let maxBoundary

function GameScreen({ chosenNumber, onGameOver }) {
  const initialGuess = generateRandomNumberBetween(1, 100, chosenNumber)
  const [currentGuess, setCurrentGuess] = useState(initialGuess)
  const [guessesAttempts, setGuessAttempts] = useState([initialGuess])

  useEffect(() => {
    if (currentGuess == chosenNumber) {
      onGameOver(guessesAttempts.length)
    }
  }, [currentGuess])

  useEffect(() => {
    minBoundary = 1
    maxBoundary = 100
  }, [])

  function nextGuessHandler(direction) {
    if (direction == 'lower') {
      maxBoundary = currentGuess
    } else if (direction == 'higher') {
      minBoundary = currentGuess + 1
    }
    console.log(minBoundary, maxBoundary, currentGuess)
    const newGuess = generateRandomNumberBetween(minBoundary, maxBoundary)
    setCurrentGuess(newGuess)
    setGuessAttempts((currGuessAttempts) => {
      return [newGuess, ...currGuessAttempts]
    })
  }

  return (
    <View style={styles.gameContainer}>
      <Title>Opponent's Guess</Title>
      <NumberContainer>{currentGuess}</NumberContainer>
      <Card>
        <InstructionText style={styles.instructionText}>
          Higher or Lower?
        </InstructionText>
        <View style={styles.buttonRowContainer}>
          <View style={styles.buttonContainer}>
            <PrimaryButton onPress={nextGuessHandler.bind(this, 'lower')}>
              <Ionicons name="md-remove" size={24} color="white" />
            </PrimaryButton>
          </View>
          <View style={styles.buttonContainer}>
            <PrimaryButton onPress={nextGuessHandler.bind(this, 'higher')}>
              <Ionicons name="md-add" size={24} color="white" />
            </PrimaryButton>
          </View>
        </View>
      </Card>
      <View dtyle={styles.guessLogContainer}>
        <FlatList
          data={guessesAttempts}
          renderItem={(guessData) => <GuessLogItem roundNumber={guessesAttempts.length - guessData.index} guess={guessData.item} />}
          keyExtractor={(guessData) => {return guessData}}
        ></FlatList>
      </View>
    </View>
  )
}

export default GameScreen

const styles = StyleSheet.create({
  gameContainer: {
    flex: 1,
    padding: 24,
  },
  buttonRowContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
  },
  buttonContainer: {
    flex: 1,
  },
  instructionText: {
    marginBottom: 12,
  },
  guessLogContainer: {
    flex: 1,
    padding: 16
  }
})
