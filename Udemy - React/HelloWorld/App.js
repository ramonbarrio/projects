import { useState } from "react";
import { StyleSheet, View, FlatList, Button } from "react-native";
import { StatusBar } from "expo-status-bar";

import GoalItem from "./components/GoalItem";
import GoalInput from "./components/GoalInput";

export default function App() {
  const [listOfGoals, setListOfGoals] = useState([]);
  const [modalIsVisible, setModalIsVisible] = useState(false)

  function startAddGoalHandler() {
    setModalIsVisible(true)
  }

  function cancelAddGoalHandler() {
    setModalIsVisible(false)
  }

  function clearGoalsHandler() {
    setListOfGoals([]);
  }

  function deleteGoalHandler(id) {
    setTimeout(() => setListOfGoals((currentListOfGoals) => {
      return currentListOfGoals.filter((item) => item.id !== id);
    }), 300)
  }

  function addGoalHandler(enteredGoalText) {
    if (
      !listOfGoals.some(
        (goalObject) => enteredGoalText.trim() === goalObject.text
      ) &&
      enteredGoalText.trim() !== ""
    ) {
      setListOfGoals((currentListOfGoals) => [
        ...currentListOfGoals,
        { text: enteredGoalText.trim(), id: Math.random().toString() },
      ]);
      setModalIsVisible(false)
      return true;
    }
    return false;
  }

  return (
    <>
      <StatusBar style="light"/>
      <View style={styles.appContainer}>
        <Button title="Add new Goal" color={"#a065ec"} onPress={startAddGoalHandler}/>
        <Button title="Clear Goals" color={"#a065ec"} onPress={clearGoalsHandler} />
        {modalIsVisible && <GoalInput modalIsVisible={modalIsVisible} onAddGoal={addGoalHandler} onCancelAddGoal={cancelAddGoalHandler}/>}
        <View style={styles.goalsContainer}>
          <FlatList
            data={listOfGoals}
            renderItem={(itemData) => {
              return (
                <GoalItem
                  text={itemData.item.text}
                  id={itemData.item.id}
                  onDeleteItem={deleteGoalHandler}
                />
              );
            }}
            keyboardShouldPersistTaps="handled"
            keyExtractor={(item, index) => {
              return item.id;
            }}
          />
        </View>
      </View>
    </>       
  );
}

const styles = StyleSheet.create({
  appContainer: {
    paddingTop: 50,
    paddingHorizontal: 16,
    flex: 1,
    backgroundColor:"#1e085a"
  },
  goalsContainer: {
    flex: 5,
  },
});
