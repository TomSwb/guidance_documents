# TypeScript React Native App Creation Guide (with Expo)

This guide walks you through creating a modern mobile app using TypeScript, React Native, and Expo. It covers setup, project structure, best practices, and essential features for a robust, maintainable app.

---

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Project Setup](#2-project-setup)
3. [Project Structure](#3-project-structure)
4. [Core Files Explained](#4-core-files-explained)
5. [Running Your App](#5-running-your-app)
6. [Adding Screens & Navigation](#6-adding-screens--navigation)
7. [Working with Assets](#7-working-with-assets)
8. [State, Logic, and TypeScript](#8-state-logic-and-typescript)
9. [Saving Data (AsyncStorage)](#9-saving-data-asyncstorage)
10. [Testing on Device or Emulator](#10-testing-on-device-or-emulator)
11. [Going Further](#11-going-further)
12. [Example: Minimal App.tsx](#12-example-minimal-apptsx)

---

## 1. Prerequisites

- **Node.js** (v18+ recommended):  
  Check with `node -v`
- **npm** (comes with Node.js):  
  Check with `npm -v`
- **Expo CLI:**  
  Install with `npm install -g expo-cli` (or use `npx expo`)
- **VS Code** (recommended editor)
- **Expo Go app** on your phone (from Google Play or App Store)

---

## 2. Project Setup

1. **Create a new Expo project with TypeScript:**
   ```bash
   npx expo init my-app
   ```
   - Choose `blank (TypeScript)` when prompted.

2. **Navigate to your project:**
   ```bash
   cd my-app
   ```

3. **Open in VS Code:**
   ```bash
   code .
   ```

---

## 3. Project Structure

A typical Expo TypeScript project looks like:

```
my-app/
│
├── App.tsx                # Main app component
├── assets/                # Images, sounds, fonts
├── src/
│   ├── screens/           # App screens (e.g., HomeScreen.tsx)
│   ├── components/        # Reusable UI components
│   ├── logic/             # Business logic (e.g., timer.ts)
│   └── navigation/        # Navigation setup (AppNavigator.tsx)
├── app.json               # Expo app configuration
├── package.json           # Dependencies and scripts
├── tsconfig.json          # TypeScript configuration
└── ...
```

---

## 4. Core Files Explained

- **App.tsx:** Entry point, sets up navigation and global providers.
- **assets/:** Store images, sounds, and fonts here.
- **src/screens/:** Each screen/page of your app.
- **src/components/:** Reusable UI elements (e.g., Button, TimerDisplay).
- **src/logic/:** App logic (e.g., timer, sound manager).
- **src/navigation/AppNavigator.tsx:** Navigation stack/tab setup.
- **app.json:** App name, icon, splash, and Expo config.
- **tsconfig.json:** TypeScript settings.

---

## 5. Running Your App

Start the Expo development server:
```bash
npx expo start
```
- Scan the QR code with Expo Go on your phone, or run on an emulator.

Stop the server with `Ctrl+C` in the terminal.

---

## 6. Adding Screens & Navigation

1. **Install navigation dependencies:**
   ```bash
   npm install @react-navigation/native @react-navigation/native-stack
   npx expo install react-native-screens react-native-safe-area-context
   ```

2. **Create a navigator (`src/navigation/AppNavigator.tsx`):**
   ```tsx
   import { NavigationContainer } from '@react-navigation/native';
   import { createNativeStackNavigator } from '@react-navigation/native-stack';
   import MainMenuScreen from '../screens/MainMenuScreen';
   import TimerScreen from '../screens/TimerScreen';

   export type RootStackParamList = {
     MainMenu: undefined;
     Timer: undefined;
   };

   const Stack = createNativeStackNavigator<RootStackParamList>();

   export default function AppNavigator() {
     return (
       <NavigationContainer>
         <Stack.Navigator initialRouteName="MainMenu">
           <Stack.Screen name="MainMenu" component={MainMenuScreen} />
           <Stack.Screen name="Timer" component={TimerScreen} />
         </Stack.Navigator>
       </NavigationContainer>
     );
   }
   ```

3. **Use your navigator in `App.tsx`:**
   ```tsx
   import AppNavigator from './src/navigation/AppNavigator';
   export default function App() {
     return <AppNavigator />;
   }
   ```

---

## 7. Working with Assets

- **Images:** Place in `assets/images/`, use with `require('../assets/images/myimage.png')`
- **Sounds:** Place in `assets/sounds/`, use with Expo AV
- **Fonts:** Place in `assets/fonts/`, load with Expo Font

Example (image):
```tsx
import { Image } from 'react-native';
<Image source={require('../assets/images/logo.png')} style={{ width: 100, height: 100 }} />
```

---

## 8. State, Logic, and TypeScript

- Use React hooks (`useState`, `useEffect`) for state.
- Use TypeScript types/interfaces for props and logic.
- Example timer logic (`src/logic/timer.ts`):

```typescript
export class Timer {
  private intervalId: NodeJS.Timeout | null = null;
  public remaining: number;

  constructor(duration: number, private onTick: (n: number) => void, private onEnd: () => void) {
    this.remaining = duration;
  }

  start() {
    this.intervalId = setInterval(() => {
      this.remaining -= 1;
      this.onTick(this.remaining);
      if (this.remaining <= 0) {
        this.stop();
        this.onEnd();
      }
    }, 1000);
  }

  stop() {
    if (this.intervalId) clearInterval(this.intervalId);
    this.intervalId = null;
  }

  pause() {
    this.stop();
  }

  resume() {
    if (!this.intervalId && this.remaining > 0) this.start();
  }
}
```

---

## 9. Saving Data (AsyncStorage)

Install AsyncStorage:
```bash
npx expo install @react-native-async-storage/async-storage
```

Example usage:
```typescript
import AsyncStorage from '@react-native-async-storage/async-storage';

// Save
await AsyncStorage.setItem('timerValue', JSON.stringify(remaining));

// Load
const value = await AsyncStorage.getItem('timerValue');
if (value !== null) {
  setRemaining(JSON.parse(value));
}
```

---

## 10. Testing on Device or Emulator

- **Expo Go app:** Scan QR code from `expo start` in your terminal.
- **Android/iOS emulator:** Press "a" or "i" in the Expo CLI web interface.

---

## 11. Going Further

- Add more screens (e.g., WorkoutList, Settings).
- Use context or Redux for global state.
- Add sound with Expo AV.
- Add custom fonts and themes.
- Build for production:  
  ```bash
  npx expo build:android
  npx expo build:ios
  ```

---

## 12. Example: Minimal App.tsx

```tsx
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Hello, Expo + TypeScript!</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, alignItems: 'center', justifyContent: 'center' },
  title: { fontSize: 32, fontWeight: 'bold' },
});
```

---

Happy coding!  
Update this guide with your notes, solutions, and tips as you build your app.