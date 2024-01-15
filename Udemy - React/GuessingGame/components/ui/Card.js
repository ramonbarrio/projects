import { StyleSheet, View } from "react-native"
import Colors from "../../constants/colors/colors"

function Card({children}) {
  return <View style={styles.inputContainer}>{children}</View>
}

export default Card

const styles = StyleSheet.create({  
  inputContainer: {
    //alignSelf: "center",
    //flex: 1,
    justifyContent: 'center',
    alignItems: 'stretch',
    marginTop: 36,
    marginHorizontal: 24,
    padding: 16,
    borderRadius: 8,
    backgroundColor: Colors.primary800,
    elevation: 8,
  }
})