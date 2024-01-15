import React from 'react';
import {Text, View} from 'react-native';
import { Colors } from 'react-native/Libraries/NewAppScreen';

export default function App() {
    return (
        <View style={{padding: 50, flexDirection: 'column', width: '60%', height: 700, justifyContent:'center', alignItems: 'stretch' }}>
            <View
                style={{
                    backgroundColor: 'red',
                    //width: 100,
                    //height: 100,
                    justifyContent: 'center',
                    alignItems: 'center',
                    flex: 1
                }}>
                <Text>Oi</Text>
            </View>
            <View
                style={{
                    backgroundColor: 'blue',
                    //width: 100,
                    //height: 100,
                    justifyContent: 'center',
                    alignItems: 'center',
                    flex: 2
                }}>
                <Text>Beleuza?</Text>
            </View>
            <View
                style={{
                    backgroundColor: 'green',
                    //width: 100,
                    //height: 100,
                    justifyContent: 'center',
                    alignItems: 'center',
                    //flex: 1
                }}>
                <Text></Text>
            </View>
        </View>
    );
}
