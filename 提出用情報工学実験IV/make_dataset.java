import java.util.Random;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Collections;

public class make_dataset {
    public static void main(String args[]) {
	Random rnd = new Random();
	int num_of_youso = 100;//人数
  int num_of_list = 5;//科目番号の数
  int youso = rnd.nextInt();
  int limnum = 20;//科目番号の上限
  List<Integer> num_list = new ArrayList<Integer>(num_of_list);


  try {
       File file = new File("tt.csv");
       BufferedWriter pw = new BufferedWriter(new FileWriter(file));

       for (int i = 0; i < num_of_youso; i++){
         for (int n = 0; n < num_of_list; n++){
              youso = rnd.nextInt(limnum);
              while (num_list.contains(youso)){ //同一の被験者が同一の科目を選択しないための処理
                youso = rnd.nextInt(limnum);
              }
              pw.write(youso + ",");
              num_list.add(youso);
              }
              num_list.clear();
              pw.newLine();
            }

          //for (int i = 0; i < num_of_youso; i++){
            //  int youso = rnd.nextInt(33);
           //System.out.println(youso);
           //pw.println(youso);

       //ファイルを閉じる
       pw.close();
   } catch (IOException e) {
       e.printStackTrace();
   }
 }
}
