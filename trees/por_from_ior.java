import java.util.Stack;

public class por_from_ior {
    static int postIndex;

    void fillPre(int[] in, int post[], int inStrt, int inEnd, Stack<Integer> s) {
        if (inStrt > inEnd)
            return;
        int val = post[postIndex];
        int inIndex = search(in, val);
        postIndex--;

        fillPre(in, post, inIndex + 1, inEnd, s);

        fillPre(in, post, inStrt, inIndex - 1, s);

        s.push(val);
    }

    void printPreMain(int[] in, int[] post) {
        int len = in.length;
        postIndex = len - 1;
        Stack<Integer> s = new Stack<Integer>();
        fillPre(in, post, 0, len - 1, s);
        while (s.empty() == false)
            System.out.print(s.pop() + " ");
    }

    int search(int[] in, int data) {
        int i = 0;
        for (i = 0; i < in.length; i++)
            if (in[i] == data)
                return i;
        return i;
    }

    public static void main(String ars[]) {
        int in[] = { 4, 10, 12, 15, 18, 22, 24, 25, 31, 35, 44, 50, 66, 70, 90 };
        int post[] = { 4, 12, 10, 18, 24, 22, 15, 31, 44, 35, 66, 90, 70, 50, 25 };
        por_from_ior tree = new por_from_ior();
        tree.printPreMain(in, post);
    }

}