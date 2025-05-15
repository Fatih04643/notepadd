import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QFontDialog

class NotDefteri(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('notdefteri.ui', self)

        self.dosya_adi = None

        # Menü eylemlerine işlevleri bağla
        self.actionOpen.triggered.connect(self.dosya_ac)
        self.actionSave.triggered.connect(self.dosya_kaydet)
        self.actionSaveAs.triggered.connect(self.dosya_farkli_kaydet)
        self.actionExit.triggered.connect(self.close)
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.actionCut.triggered.connect(self.textEdit.cut)
        self.actionCopy.triggered.connect(self.textEdit.copy)
        self.actionPaste.triggered.connect(self.textEdit.paste)
        self.actionFontSize.triggered.connect(self.yazi_boyutu_ayarla)

    def dosya_ac(self):
        options = QFileDialog.Options()
        dosya_adi, _ = QFileDialog.getOpenFileName(self, "Dosya Aç", "", "Metin Dosyaları (*.txt);;Tüm Dosyalar (*)", options=options)
        if dosya_adi:
            try:
                with open(dosya_adi, 'r', encoding='utf-8') as f:
                    icerik = f.read()
                    self.textEdit.setText(icerik)
                    self.dosya_adi = dosya_adi
                    self.setWindowTitle(f"{self.dosya_adi} - Not Defteri")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Dosya okuma hatası: {e}")

    def dosya_kaydet(self):
        if self.dosya_adi:
            try:
                icerik = self.textEdit.toPlainText()
                with open(self.dosya_adi, 'w', encoding='utf-8') as f:
                    f.write(icerik)
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Dosya yazma hatası: {e}")
        else:
            self.dosya_farkli_kaydet()

    def dosya_farkli_kaydet(self):
        options = QFileDialog.Options()
        dosya_adi, _ = QFileDialog.getSaveFileName(self, "Farklı Kaydet", "", "Metin Dosyaları (*.txt);;Tüm Dosyalar (*)", options=options)
        if dosya_adi:
            try:
                icerik = self.textEdit.toPlainText()
                with open(dosya_adi, 'w', encoding='utf-8') as f:
                    f.write(icerik)
                self.dosya_adi = dosya_adi
                self.setWindowTitle(f"{self.dosya_adi} - Not Defteri")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Dosya yazma hatası: {e}")

    def yazi_boyutu_ayarla(self):
        font, ok = QFontDialog.getFont(self.textEdit.font(), self)
        if ok:
            self.textEdit.setFont(font)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    not_defteri = NotDefteri()
    not_defteri.show()
    sys.exit(app.exec_())