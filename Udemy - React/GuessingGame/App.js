import { useState, useEffect, useCallback } from "react";
import { ImageBackground, StyleSheet, SafeAreaView, StatusBar } from "react-native";
import StartGameScreen from "./screens/StartGameScreen";
import { LinearGradient } from "expo-linear-gradient";
import GameScreen from "./screens/GameScreen";
import Colors from "./constants/colors/colors";
import GameOver from "./screens/GameOver";
import {useFonts} from "expo-font"
import * as SplashScreen from 'expo-splash-screen'

SplashScreen.preventAutoHideAsync();

export default function App() {
  const [userNumber, setUserNumber] = useState()
  const [gameIsOver, setGameIsOver] = useState(false)
  const [guessRounds, setGuessRounds] = useState(0)
  const [fontsLoaded] = useFonts({
    'open-sans': require('./assets/fonts/OpenSans-Regular.ttf'),
    'open-sans-bold': require('./assets/fonts/OpenSans-Bold.ttf')
  })

  const onLayoutRootView = useCallback(async () => {
    if (fontsLoaded) {
      await SplashScreen.hideAsync()
    }
  }, [fontsLoaded])

  if(!fontsLoaded) {
    return null
  }

  function pickedNumberHandler(pickedNumber) {
    setUserNumber(pickedNumber)
  }

  function gameOverHandler(numberOfRounds) {
    setGameIsOver(true)
    setGuessRounds(numberOfRounds)
  }

  function resetGameHandler() {
    setUserNumber(null)
    setGameIsOver(false)

    console.log("Oi")
  }

  let screen = <StartGameScreen onPickNumber={pickedNumberHandler}/>

  if (userNumber) {
    screen = <GameScreen chosenNumber={userNumber} onGameOver={gameOverHandler}/>
  }

  if (gameIsOver) {
    screen = <GameOver userNumber={userNumber} guessesAttempts={guessRounds} onResetGame={resetGameHandler}/>
  }

  return (
    <LinearGradient colors={[Colors.primary700, Colors.accent500]} style={styles.rootScreen} onLayout={onLayoutRootView}>
      <ImageBackground
        source={require("./assets/images/background.png")}
        resizeMode="cover"
        style={styles.rootScreen}
        imageStyle={styles.backgroundImage}
      >
        <SafeAreaView style={styles.androidSafeAreaView}>
          {screen}
        </SafeAreaView>
      </ImageBackground>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  rootScreen: {
    flex: 1,
  },
  backgroundImage: {
    opacity: 0.15
  },
  androidSafeAreaView: {
    flex: 1,
    paddingTop: Platform.OS === "android" ? StatusBar.currentHeight : 0
  }
});
