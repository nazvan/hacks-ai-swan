import { contextBridge } from 'electron'
import { BrowserWindow } from '@electron/remote'
import path from 'path'
import { enable } from '@electron/remote/main'

let imageWindow

contextBridge.exposeInMainWorld('myWindowAPI', {
  minimize () {
    BrowserWindow.getFocusedWindow().minimize()
  },

  toggleMaximize () {
    const win = BrowserWindow.getFocusedWindow()

    if (win.isMaximized()) {
      win.unmaximize()
    } else {
      win.maximize()
    }
  },

  close () {
    BrowserWindow.getFocusedWindow().close()
  },

  openImage (data: string) {
    imageWindow = new BrowserWindow({
      icon: path.resolve(__dirname, 'icons/icon.png'), // tray icon
      maximizable: true,
      webPreferences: {
        contextIsolation: true,
        // More info: https://v2.quasar.dev/quasar-cli-vite/developing-electron-apps/electron-preload-script
        preload: path.resolve(__dirname, process.env.QUASAR_ELECTRON_PRELOAD),
        sandbox: false
      },
    });
    imageWindow.maximize()
    enable(imageWindow.webContents)
    imageWindow.loadURL(data);
  },

  closeImg () {
    if (imageWindow) {
      imageWindow.close()
    }
  }
})
