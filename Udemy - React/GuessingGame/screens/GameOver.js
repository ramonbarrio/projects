import { View, Image, StyleSheet, Text } from 'react-native'
import Title from '../components/ui/Title'
import Colors from '../constants/colors/colors'
import PrimaryButton from '../components/ui/PrimaryButton'

function GameOver({userNumber, guessesAttempts, onResetGame}) {
  return (
    <View style={styles.rootContainer}>
      <Title> Game Over </Title>
      <View style={styles.imageContainer}>
        <Image
          style={styles.image}
          source={require('../assets/images/success.png')}
        />
      </View>
      <Text style={styles.summaryText}>
        Your phone needed <Text style={styles.highlight}>{guessesAttempts}</Text> rounds to
        guess the number <Text style={styles.highlight}>{userNumber}.</Text>
      </Text>
      <PrimaryButton onPress={onResetGame}>Start New Game</PrimaryButton>
    </View>
  )
}

export default GameOver

const styles = StyleSheet.create({
  rootContainer: {
    flex: 1,
    padding: 24,
    alignItems: 'center',
    justifyContent: 'center',
  },
  imageContainer: {
    width: 200,
    height: 200,
    borderRadius: 100,
    borderWidth: 3,
    borderColor: Colors.primary800,
    overflow: 'hidden',
    margin: 36,
  },
  image: {
    width: '100%',
    height: '100%',
  },
  summaryText: {
    fontFamily: 'open-sans',
    fontSize: 24, 
    textAlign: 'center',
    marginVertical: 24
  },
  highlight: {
    fontFamily: 'open-sans-bold',
    color: Colors.primary800,
    fontSize: 24,
  },
})
