import { Button, Text, View } from "react-native"
import Board from "../components/Board"
import { useState } from "react"
import InitialBoard from "../constants/colors/InitialBoard"
import CapturablePieccesByType from "../constants/colors/CaptuarablePiecesByType"

function GameScreen({playerOneName, playerTwoName, onExitGame}) {

  const [playerTurn, setPlayterTurn] = useState('playerOne')
  const [selectedTile, setSelectedTile] = useState(null)
  const [selectedPiece, setSelectedPiece] = useState(null)
  const [boardPosition, setBoardPosition] = useState(InitialBoard)

  function handlePressOwnPiece(row, column, pieceInPressedTile) {
    setSelectedTile({row, column})
    setSelectedPiece(pieceInPressedTile)
  }

  function handleMakeMove(row, column, terrain) {
    const printColor = playerTurn == 'playerOne' ? 'White' : 'Black'
    console.log('den color prohibited: ' + printColor)
    if (terrain.type == 'Grass' || terrain.type == 'Trap' || (terrain.type == 'Den' && terrain.color != (playerTurn == 'playerOne' ? 'White' : 'Black')) || (terrain.type == 'Water' && selectedPiece.type == 'Rat')) {
      setBoardPosition((currBoard) => {
        const newBoard = currBoard.slice()
        newBoard[selectedTile.row][selectedTile.column] = null
        newBoard[row][column] = selectedPiece
        return newBoard
      })
      setSelectedPiece(null)
      setSelectedTile(null)
      setPlayterTurn((currPlayer) => {
        return currPlayer == 'playerOne' ? 'playerTwo' : 'playerOne'
      })
    } else {
      setSelectedPiece(null)
      setSelectedTile({row, column})
    }
  }

  function handleMakeCapture(row, column, pieceInPressedTile, terrain) {
    if (terrain.type != 'Water' || (terrain.type == 'Water' && selectedPiece.type == 'Rat')) {
      if (CapturablePieccesByType[selectedPiece.type].includes(pieceInPressedTile.type)) {
        setBoardPosition((currBoard) => {
          const newBoard = currBoard.slice()
          newBoard[selectedTile.row][selectedTile.column] = null
          newBoard[row][column] = selectedPiece
          return newBoard
        })
        setSelectedPiece(null)
        setSelectedTile(null)
        setPlayterTurn((currPlayer) => {
          return currPlayer == 'playerOne' ? 'playerTwo' : 'playerOne'
        })
      } else {
        setSelectedPiece(null)
        setSelectedTile({row, column})
      }
    console.log('oi')
    }
  }

  function handlePressAdjacent(row, column, pieceInPressedTile, terrain) {
    if (!pieceInPressedTile) {
      handleMakeMove(row, column, terrain)
    } else {
      handleMakeCapture(row, column, pieceInPressedTile, terrain)
    }    
  }

  function handlePressTile(row, column, terrain) {
    const pieceInPressedTile = boardPosition[row][column]
    const pieceInPressedTileIsCurrentPlayers = (!!pieceInPressedTile && pieceInPressedTile.color == 'White' && playerTurn == 'playerOne') || (!!pieceInPressedTile && pieceInPressedTile.color == 'Black' && playerTurn == 'playerTwo') 
    const pieceInPressedTileIsOpponentPlayers = (!!pieceInPressedTile && pieceInPressedTile.color == 'Black' && playerTurn == 'playerOne') || (!!pieceInPressedTile && pieceInPressedTile.color == 'White' && playerTurn == 'playerTwo') 
    if (pieceInPressedTileIsCurrentPlayers) {
      handlePressOwnPiece(row, column, pieceInPressedTile) //se clicar na propria peca nao importa o estado anterior, seleciona essa peca e esse tile
    } else if (!selectedPiece) { //se nao for sua peca e nao tiver uma selecionada, seleciona esse tile
      setSelectedTile({row, column})
    } else { //se nao clicou na sua peca e tem peca selecionada
        const isPressedTileAdjacentToSelectedPiece = (selectedTile.row == row && [selectedTile.column+1, selectedTile.column-1].includes(column)) || (selectedTile.column == column && [selectedTile.row+1, selectedTile.row-1].includes(row))
        if (isPressedTileAdjacentToSelectedPiece) {
          handlePressAdjacent(row, column, pieceInPressedTile, terrain)
        } else {
          //handlePressApart()
          console.log('Hi')
        }
      }
  }


  return (
    <View>
      <View style={{flexDirection:'row'}}>
        <View>
          <Board selectedTile={selectedTile} boardPosition={boardPosition} onPressTile={handlePressTile}/>
        </View>
        <View>
          <Text>{playerOneName}</Text>  
          <Text>{playerTwoName}</Text>
        </View>
      </View>
      <View>
        <Button title="Exit" onPress={onExitGame}/>
      </View>
    </View>
  )
}

export default GameScreen