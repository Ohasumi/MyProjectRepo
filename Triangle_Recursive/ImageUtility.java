import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

//Just use to demonstrate the array result in image
public class ImageUtility {
    public static void writeImage(int[][] arr) {
        String path = "C:\\Users\\white\\Desktop\\IntelliJ\\untitled\\src\\" + "Picture" + ".png";
        BufferedImage image = new BufferedImage(arr.length, arr[0].length, BufferedImage.TYPE_INT_RGB);
        for (int x = 0; x < arr.length; x++) {
            for (int y = 0; y < arr.length; y++) {
                if (arr[x][y] == 0)

                    image.setRGB(y, x, 0xFFFFFF);

                else
                    image.setRGB(y, x, 0xFF0404);


            }
            //System.out.print("\n");
        }

        File ImageFile = new File(path);
        try {
            ImageIO.write(image, "png", ImageFile);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

//Source code for image function ( James Crocker & michaelb958--GoFundMonica): https://stackoverflow.com/a/17366143
