import { View } from "react-native";
import Tile from "./Tile";
import BoardTerrain from "../constants/colors/BoardTerrain";
import BoardColors from "../constants/colors/BoardColors";
import { useState } from "react";
import InitialBoard from "../constants/colors/InitialBoard";

function Board({selectedTile, boardPosition, onPressTile}) {

  function handlePressTile(row, column, terrain) {
    onPressTile(row, column, terrain)
  }

  function getTileColor(row, column, terrain) {
    if ((!!selectedTile?.row || selectedTile?.row == 0) && selectedTile.row == row && (!!selectedTile?.column || selectedTile?.column == 0) && selectedTile.column == column) {
      return BoardColors.Selected
    } else {
      if (['Grass', 'Water'].includes(terrain.type)){
        return BoardColors[terrain.color + terrain.type]
    } else {
      return BoardColors[terrain.type]
    }}
  }

  return (
    <View style={{flexDirection:'row'}}>
      {[0,1,2,3,4,5,6].map((column) => {
        return (
          <View key={column}>
            {[0,1,2,3,4,5,6,7,8].map((row) => {
              const piece = boardPosition[row][column]
              const terrain = BoardTerrain[row][column]
              const color = getTileColor(row, column, terrain)
              return (
                <Tile key={column*8 + row} row={row} column={column} color={color} piece={piece} terrain={terrain} onPressTile={handlePressTile}/>
              )
            })}
          </View>
        )
      })}
    </View>
  )
}

export default Board