import { useState } from "react";
import { StatusBar } from "expo-status-bar";
import { StyleSheet, View } from "react-native";
import StartScreen from "./screens/StartScreen";
import GameScreen from "./screens/GameScreen";
import Colors from "./constants/colors/Colors";
import Board from "./components/Board";

export default function App() {
  const [isGameRunning, setIsGameRunning] = useState(false);
  const [playerOneName, setPlayerOneName] = useState("");
  const [playerTwoName, setPlayerTwoName] = useState("");

  function startGameHandler(
    newPlayerOneName: string,
    newPlayerTwoName: string
  ) {
    setPlayerOneName(newPlayerOneName);
    setPlayerTwoName(newPlayerTwoName);
    setIsGameRunning(true);
  }

  function ExitGameHandler() {
    setIsGameRunning(false);
  }

  let screen = <StartScreen onPressPlay={startGameHandler} />;

  if (isGameRunning) {
    screen = (
      <GameScreen
        playerOneName={playerOneName}
        playerTwoName={playerTwoName}
        onExitGame={ExitGameHandler}
      />
    );
  }

  return (
    <View style={styles.container}>
      {screen}
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#ffffff",
    alignItems: "center",
    justifyContent: "center",
  },
});
