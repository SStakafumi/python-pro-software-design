# Chapter 2
- 「from <モジュール名> import *」という構文でモジュール内のすべての名前をインポートできるが名前の衝突が起こる可能性がありデバックを難しくする可能性があるため推奨されない.

- IDE(統合開発環境)によっては組み込みのものと同じ名前を使うと警告してくれるため衝突を避けることができる. 

- 関心(concern)の分離の手段として関数, クラスにまとめる手法がある. クラスのメソッドと属性の関係性が強い「凝集度」の高いクラスほど好ましい. 

- あるクラスが別のクラスに依存している「結合(coupled)」状態や別のクラスの変更に影響を受けるように詳細に依存している「密結合(tightly-coupled)」状態は理想でなく, 開発の最終段階では「疎結合」の状態が望まれる

- Pythonにおいては, モジュール(.pyファイル)を含むディレクトリをパッケージと呼ぶ. 「\_\_init\_\_.py」という特別なファイルが必要. 

# Chapter 3
- Pythonではカプセル化のためにクラスやモジュールが使用される。

- Pythonで最も大きいカプセル化の単位はパッケージであり、Python Package Index (PyPI) として公開されている。

- Pythonでは真の意味でのプライベートなメソッドやデータは存在しないが一般的に使われている「規約」がある。例えば、クラス内での利用を意図されたメソッドや変数の場合は前に「_」をつける.

- 手続き型プログラミング
    - 「関数」とよばれることの多い、手続き的な機能の呼び出しが多様される。多くの場合入力(引数)に依存して処理を行う。
- 関数型プログラミング
    - プログラムを「関数を合成したもの」と考える。関数が他の関数を引数としてとったり、戻り値として関数を返したりする。
- 宣言型プログラミング
    - タスクのパラメータを宣言。

- 継承関係だけで記述するのが難しい場合、特徴を独立にしておくことで必要に応じて合成する手段をとることができる。合成は通常プログラミング言語の「インターフェース」という機構を用いて実現できる。インターフェースはクラスが実装しなければならないメソッドとデータの形式的な定義のこと。

- Pythonはインターフェース機構を持っていないが、ダッグタイピングと多重継承によって実現される。Pythonは複数のクラスの継承が可能なためこれによりインターフェースが実現できる。この機能を「ミックスイン(mixin)」と呼ぶ。

# Chapter 4
- 時間計算量
    - 入力データとの関係でどの程度速く処理できるかのい尺度.
- 空間計算量
    - 入力のサイズが大きくなるに伴ってディスクスペースあるいはメモリをどの程度使用するかを表すもの。Pythonではメモリ管理を処理系が (基本的に) 自動で行うため、意識することが少ない。Pythonではガーベッジコレクション (使わなくなったオブジェクト用に割り当てられたメモリの開放) が自動的に行われる。
    - メモリを大量に消費してしまう典型的な例は必要ないにも関わらず巨大なデータファイルをメモリに読み込んでしまうこと。
    - ディスク容量の問題はすぐに表面化しないことがあるため、場合によっては対処が困難になる。

- 定数オーダーのデータ型
    - Pythonの辞書, 集合 (set) は追加、削除、アクセスに関しては定数時間で終わる。

- 線形時間のデータ型
    - Pythonのリストを操作する処理の多くはO(n)になる。最後の要素の削除、最後への要素の追加はO(1)となる

- Pythonではジェネレータを使うことで、リクエストされるたびに一項目ずつ値を生成することができる。値を一度に一つ生成 (yield) することで、メモリに全要素を記憶せずに処理を行える。つまり、ジェネレータはメモリ内に一要素分のみのデータを保存し、続く要素は次回要求された時に初めて生成する。例えばrange()はジェネレータであり, range(100_000_000)などのコードでは大量のメモリを占有しているわけではなく、その範囲の値をひとつずつ生成している。yeildはreturnと同じように値を返しその関数はいったんそこで実行を停止するが、次回はその次の要素から開始される。可能ならリストよりジェネレータを使うべき。
    ```python
    # rangeの処理をまねたジェネレータ

    def range(*args):
        if len(args) == 1:
            start = 0
            stop = args[0]
        else:
            start = args[0]
            stop = args[1]
        
        current = start

        while current < stop:
            yield current
            current += 1
    ```

- Pythonのtimeitモジュールを使うとコードの実行時間を計測できる。バッテリ残量やCPUのクロックスピードなどにも影響されるためtimeitは繰り返し実行し、平均的なパフォーマンスを確認すべき。

- cProfileモジュールはメソッドや関数にかんして何度呼び出されたか、呼び出しで合計どのくらいの時間が消費されたかなどの情報を出力する。