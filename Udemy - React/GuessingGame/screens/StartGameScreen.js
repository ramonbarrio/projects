import { useState } from 'react'
import { View, TextInput, StyleSheet, Alert } from 'react-native'
import PrimaryButton from '../components/ui/PrimaryButton'
import Colors from '../constants/colors/colors'
import Title from '../components/ui/Title'
import Card from '../components/ui/Card'
import InstructionText from '../components/ui/InstructionsText'

function StartGameScreen({onPickNumber}) {
  const [enteredNumber, setEnteredNumber] = useState('')

  function numberInputHandler(enteredText) {
    setEnteredNumber(enteredText)
  }

  function resetInputHandler() {
    setEnteredNumber('')
  }

  function confirmInputHandler() {
    const chosenNumber = parseInt(enteredNumber)
    if (isNaN(chosenNumber)) {
      Alert.alert('Invalid input!', 'It must a number between 1 and 99.', [
        { text: 'Okay', style: 'destructive', onPress: resetInputHandler },
      ])
      return
    }
    if (chosenNumber <= 0 || chosenNumber > 99) {
      Alert.alert('Invalid number!', 'It has to be between 1 and 99.', [
        { text: 'Okay', style: 'destructive', onPress: resetInputHandler },
      ])
      return
    }

    onPickNumber(chosenNumber)

  }

  return (
    <View style={styles.rootContainer}>
      <Title> Guessing Game </Title>
      <Card>
        <InstructionText style={styles.InstructionText}>Enter a Number</InstructionText>
        <TextInput
          style={styles.numberInput}
          maxLength={2}
          keyboardType="number-pad"
          autoCapitalize="none"
          autoCorrect={false}
          value={enteredNumber}
          onChangeText={numberInputHandler}
        />
        <View style={styles.buttonRowContainer}>
          <View style={styles.buttonContainer}>
            <PrimaryButton onPress={resetInputHandler}>Reset</PrimaryButton>
          </View>
          <View style={styles.buttonContainer}>
            <PrimaryButton onPress={confirmInputHandler}>Confirm</PrimaryButton>
          </View>
        </View>
      </Card>
    </View>
  )
}

export default StartGameScreen

const styles = StyleSheet.create({
  rootContainer: {
    flex: 1,
    marginTop: 100,
    alignItems: 'center'
  },
  buttonRowContainer: {
    //flex: 1,
    flexDirection: 'row',
    justifyContent: 'space-evenly',
    alignItems: 'center',
  },
  buttonCollumnContainer: {
    flexDirection: 'column',
    alignItems: 'stretch',
    justifyContent: 'space-between',
    flex: 1,
  },
  buttonContainer: {
    //flex: 0.4
    width: '40%',
  },
  numberInput: {
    height: 50,
    width: 50,
    textAlign: 'center',
    fontSize: 32,
    borderBottomColor: Colors.accent500,
    borderBottomWidth: 2,
    color: Colors.accent500,
    marginVertical: 8,
    fontWeight: 'bold',
    alignSelf: 'center',
  },
})
