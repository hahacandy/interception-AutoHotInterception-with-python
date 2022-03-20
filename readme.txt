これは何？
：自分のパソコンに繋いであるhid装置（mouse, keyboard等）に直接信号(キーボードの入力、マウスのクリック等)を送ることができるコード

なぜ使う？
：ソフトウェア的な信号ではないのでゲームでも操作ができる



1.
https://github.com/oblitum/Interception/releases
圧縮を解凍して
Interception\command line installer\install-interception.exe を設置して再起動


2.
https://github.com/evilC/AutoHotInterception
圧縮を解凍して
AutoHotInterception\Lib　の中に
Interception\library　を全部上書きする


3.
AutoHotInterception\Monitor.ahk
ファイルを起動したら
今パソコンにつながっている keyboard,mouse 等の番号が見える


4.
環境設定
Python 3.8.10
pip install pythonnet==2.5.2, keyboard, pyautogui


5.
環境設定2

AutoHotInterception\Lib\AutoHotInterception.dll

32bitの場合
C:\Users\desk\Downloads\Interception\library\x32\interception.dll
C:\Users\desk\Downloads\Interception\library\x32\interception.lib

64bitの場合
C:\Users\desk\Downloads\Interception\library\x64\interception.dll
C:\Users\desk\Downloads\Interception\library\x64\interception.lib

総3個のファイルをこのフォルダーにコピペする