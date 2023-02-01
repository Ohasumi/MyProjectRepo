/*
    Author: Thanakit Yuenyongphisit
    Purpose: To Draw triangle with inverted triangle recursively in 2D array
    Date: 1/02/2023

 */


public class TriangleRecursive {
    public static void TriangleDraw(int[][] arr, int x, int y, int length, int depth){
        //Draw triangle
        int count = 0;//To find middle of triangle
        for(int i = x; i < x+length; i++){//Row
            for(int j = y; j < y+length; j++){//Col
                if(j <= count)
                    arr[i][j] = 1;
                else
                    arr[i][j] = 0;
            }
            //To set how much it extend in each column ( draw the horizontal line)
            if (i < length/2){
                count += 2;

            }
            else{
                count -= 2;

            }

        }
        //This part are draw the inverted triangle with other color
        //Recursive part
        recur(arr,x,y,length, depth);
    }
    public static void recur(int[][] arr, int x, int y, int length, int depth){
        //Base case
        if (depth == 0)
            return;
        //Inverted
        //Find edge
        int x_top = (x + (x + length/2))/2;
        int x_bot = ((x+ length) + (x + length/2))/2;

        int invCount= 0;
        int y_start = (y+y+length)/2;
        for( int i = x_top; i <= x_bot ; i++){
            for (int j = y_start; j >= y ; j--){
                if(y_start - j > invCount)
                    break;

                arr[i][j] = 0;
            }

            //Update count
            if (i < (x + x + length)/2)
                invCount += 2;
            else
                invCount -=2;
        }

        //Recursive
        //Top
        recur(arr,x,y,Math.round((length/2f)),depth - 1);

        //bot
        recur(arr,x + length/2, y,Math.round((length/2f)),depth - 1);

        //right

        recur(arr,(x + (x + length/2))/2 ,(y+(y+length))/2,Math.round((length/2f)),depth - 1);

    }
}
