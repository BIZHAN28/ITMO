import java.util.Random;

public class Main {
	public static void main(String[] args) {
	    
	    	Random rand = new Random();
		short[] a = new short[18];
		float[] x = new float[11];
		double[][] an = new double[18][11];
		double[] check = {2, 4, 5, 6, 10, 11, 12, 14, 19};
		boolean m = false;
		
		for (short i = 2; i < 20; i++) {
		    a[i-2] = i;
		}
		for (int i = 0; i < 11; i++) {
		    x[i] = rand.nextFloat() * 14 - 5;
		}
		for (int i = 0; i < 18; i++) {
		    if (a[i] == 13) {
                	for (int j = 0; j < 11; j++) {
		            an[i][j] = Math.tan(Math.pow(2 + Math.pow(x[j]/12, x[j]), 2));
               		}
                m = true;
		    }
		    for (int j = 0; j < check.length; j++) {
		        if (a[i] == check[j]) {
		            for (int k = 0; k < 11; k++) {
		                an[i][k] = Math.pow(2/3*(Math.pow(Math.pow(x[j], x[j] - 1) / (1 - 3/4*(0.5 - x[j])), 2) + 1), 3);
		            }
		            m = true;
                }
	        }
            if (m == false) {
                for (int j = 0; j < 11; j++) {
		            an[i][j] = Math.pow((Math.sin(Math.sin(Math.pow(2/3 + x[j], 3)))/Math.PI), Math.pow(x[j]/6, 1/3));
                }
            }
            m = false;
		}
		for (int i = 0; i < 18; i++) {
		    for (int j = 0; j < 11; j++) {
		        System.out.printf("%.4f", an[i][j]);
		        System.out.print(" ");
		    }
		}
		        
	}
}
