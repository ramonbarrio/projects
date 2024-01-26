import { useState } from "react";
import { Modal, View, TextInput, Button, StyleSheet, Image } from "react-native";

function GoalInput(props) {
  function goalInputHandler(enteredText) {
    setEnteredGoalText(enteredText);
  }

  function addGoalHandler() {
    const wasGoalAdded = props.onAddGoal(enteredGoalText);
    if (wasGoalAdded) {
      setEnteredGoalText("");
    }
  }

  const [enteredGoalText, setEnteredGoalText] = useState("");
  return (
    <Modal visible={props.modalIsVisible} animationType="slide">
      <View style={styles.inputContainer}>
        <Image style={styles.image} source={require("../assets/images/goal.png")} />
        <TextInput
          ref={(input) => {
            this.textInput = input;
          }}
          style={styles.textInput}
          placeholder="Your Goal"
          onChangeText={goalInputHandler}
          value={enteredGoalText}
        />
        <View style={styles.inputButtonContainer}>
          <View style={styles.inputButton}>
            <Button title="Cancel" onPress={props.onCancelAddGoal} color="#f32182"/>
          </View>
          <View style={styles.inputButton}>
            <Button title="Add Goal" onPress={addGoalHandler} color="#5e0acc"/>
          </View>
        </View>
      </View>
    </Modal>
  );
}

export default GoalInput;

const styles = StyleSheet.create({
  inputContainer: {
    flex: 1,
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    borderBottomWidth: 1,
    borderBottomColor: "#cccccc",
    backgroundColor: "#311b6b"
  },
  textInput: {
    borderWidth: 1,
    borderColor: "#e4d0ff",
    backgroundColor: "#e4d0ff",
    color: "#120438",
    width: "80%",
    marginRight: 8,
    padding: 16,
    borderRadius: 8
  },
  inputButtonContainer: {
    flexDirection: "row",
    margin: 8,
    justifyContent: "center",

  },
  inputButton: {
    margin: 4,
    width: "40%",
  },
  image: {
    width: 100,
    height: 100,
    margin: 20,
  }

});
