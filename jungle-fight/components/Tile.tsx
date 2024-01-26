import { View, StyleSheet, Text, Pressable } from "react-native";
import Colors from "../constants/colors/Colors";

type TileProps = {
    row: number, 
    column: number, 
    color: string, 
    piece: string, 
    onPressTile: () => void,
    terrain: string
  }

function Tile({row, column, color, piece, onPressTile, terrain}: TileProps) {
  const textColor = 'black'
  return (
    <View style={[styles.tile, {backgroundColor: color}]}>
      <Pressable style={{flex:1}} onPress={onPressTile.bind(this, row, column, terrain)}>
        <View style={{flex: 1}}>
          {piece && <Text style={{color:textColor, fontSize: 8}}>{JSON.stringify(piece)}</Text>}
        </View>
      </Pressable>
    </View>  
  )
}

export default Tile

const styles = StyleSheet.create({
  tile: {
    width:50,
    height:50,
  }
  
})