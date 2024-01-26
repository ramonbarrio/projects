import {View, Text, TextInput, Button} from 'react-native'
import Colors from '../constants/colors/Colors'
import Tile from '../components/Tile';
import Board from '../components/Board'
import { useState } from 'react';

function StartScreen({onPressPlay}) {
  const [playerOneInput, setPlayerOneInput] = useState('')
  const [playerTwoInput, setPlayerTwoInput] = useState('')
  
  function playerOneInputHandler(enteredText: string) {
    setPlayerOneInput(enteredText);
  }
  function playerTwoInputHandler(enteredText: string) {
    setPlayerTwoInput(enteredText);
  }

  return (
  <View>
    <Text style={{color: Colors.pink.Gold, fontSize: 36, fontWeight: 'bold' }}> JungleFight </Text>
    <TextInput placeholder="Player 1" value={playerOneInput} onChangeText={playerOneInputHandler}/>
    <TextInput placeholder="Player 2" value={playerTwoInput} onChangeText={playerTwoInputHandler}/>
{/*     <Tile color={Colors.pink.Pink}/>
    <Tile color={Colors.pink.Gold}/>
    <Tile color={Colors.pink.HotPink}/>
    <Tile color={Colors.pink.MediumPurple}/>
    <Tile color={Colors.pink.MediumVioletRed}/>
    <Tile color={Colors.pink.LightPink1}/>
    <Tile color={Colors.pink.LightPink2}/> */}
    <Button title="Play" onPress={onPressPlay.bind(this, playerOneInput, playerTwoInput)}/>
  </View>
  )
}

export default StartScreen;
