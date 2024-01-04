object Solution {
    def maxAreaOfIsland(board: Array[Array[Int]]): Int = {
        val m = board.length
        if (m == 0) return 0
        val n = board(0).length   
        var maxi = 0
        var area = 0
        val directions = List((-1,0), (1,0), (0,1), (0,-1))
        def dfs(i:Int, j:Int):Unit = {
            if (i < 0 || j < 0 || i >=m || j >=n || board(i)(j) == 0){
                return
            }
            area += 1
            maxi = maxi max area
            board(i)(j) = 0
            directions.foreach({
                 case (stepI:Int, stepJ:Int) => 
                    dfs(i + stepI, j + stepJ)
            })
        }

        for (i<- 0 until m){
            for (j <- 0 until n){
                if (board(i)(j) == 1){
                    dfs(i,j)
                    area = 0
                }
            }
        }
        maxi
    }
}