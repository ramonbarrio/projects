import { Text } from "react-native"
import Colors from "../../constants/colors/colors"

function Title({children}) {
  return (
<Text style={styles.title}>{children}</Text>
  )
}
export default Title

const styles = {
  title: {
    fontFamily: "open-sans-bold",
    fontSize: 28,
    //fontWeight: "bold",
    color: Colors.accent500,
    textAlign: "center",
    borderWidth:2,
    borderColor: Colors.accent500
  }
}