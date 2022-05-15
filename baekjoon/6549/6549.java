import java.awt.*;
import java.util.ArrayList;
import java.util.Scanner;

class Main {

    private final Long[] hist;
    private final Integer[] tree;
    int MAX_INT = 0x7fffffff;

    public Main(ArrayList<Long> hist) {
        this.hist = hist.toArray(new Long[0]);
        this.tree = new Integer[hist.size()*4];
        this.construct_tree(1,0, hist.size()-1);
    }

    private Integer getLessHeightIndex(int ... indices) {
        long minHeight = 0x7fffffff;
        int minIndex = 0x7fffffff;
        for(int index: indices) {
            if(index >= this.hist.length)
                continue;
            if(minHeight > this.hist[index]) {
                minHeight = this.hist[index];
                minIndex = index;
            }
        }
        return minIndex;
    }

    private Integer construct_tree(int treeNode, int left, int right) {
        if (left == right) {
            this.tree[treeNode] = left;
            return left;
        }

        int mid = (left + right) / 2;
        int left_index = construct_tree(treeNode*2, left, mid);
        int right_index = construct_tree(treeNode*2+1, mid+1, right);

        this.tree[treeNode] = this.getLessHeightIndex(left_index, right_index);
        return this.tree[treeNode];
    }

    private Integer query(int left, int right, int treeNode, int treeLeft, int treeRight) {

        if (right < treeLeft || treeRight < left)
            return MAX_INT;
        if (left <= treeLeft && treeRight <= right)
            return this.tree[treeNode];

        int treeMid = (treeLeft + treeRight) / 2;
        int left_index = query(left, right, treeNode*2, treeLeft, treeMid);
        int right_index = query(left, right, treeNode*2+1, treeMid+1, treeRight);
        return getLessHeightIndex(left_index, right_index);
    }

    public Integer query(int left, int right) {
        return this.query(left, right, 1, 0, this.hist.length-1);
    }

    private long get_max_area(int left, int right) {
        if (left == right) {
            return this.hist[left];
        }

        int minHeightIndex = this.query(left, right);
        long area = (right-left+1)*this.hist[minHeightIndex];
        if (left <= minHeightIndex-1) {
            long left_area = get_max_area(left, minHeightIndex-1);
            area = Math.max(left_area, area);
        }
        if (right >= minHeightIndex+1) {
            long right_area = get_max_area(minHeightIndex+1, right);
            area = Math.max(right_area, area);
        }
        return area;
    }

    public long get_max_area() {
        return get_max_area(0, this.hist.length-1);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        ArrayList<Long> hist = new ArrayList<>();

        // 1725 맞았습니다!
        /* int n = sc.nextInt();
        for(int i=0;i<n;i++) {
            hist.add(sc.nextInt());
        }
        Main main = new Main(hist);
        System.out.println(main.get_max_area()); */

        // 6549 틀렸습니다!
        while(true) {
            hist = new ArrayList<>();
            String line = sc.nextLine();
            line = line.trim();
            String[] values = line.split(" +");
            for(String value : values)
                hist.add(Long.parseLong(value));
            if (hist.size() == 1 && hist.get(0) == 0)
                break;
            hist.remove(0);

            Main main = new Main(hist);
            System.out.println(main.get_max_area());
        }
    }
}
