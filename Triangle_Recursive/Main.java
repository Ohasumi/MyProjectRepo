/*
    Author: Thanakit Yuenyongphisit
    Purpose: To demonstrate TriangleRecursive class
    Date: 1/02/2023

 */
public class Main {
    public static void main(String[] args) {

        int x = 0;
        int y = 0;
        int length = 1111;
        int depth = 4;
        int[][] arr = new int[length][length];

        TriangleRecursive.TriangleDraw(arr,0,0,length, depth);

        ImageUtility.writeImage(arr);



    }
}
