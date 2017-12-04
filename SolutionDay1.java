import java.util.*;
public class SolutionDay1
{
	public static int recFindAnswer(String s, int lower, int upper)
	{
		//base case
		if(lower == upper - 1)
			return 0;
		char a = s.charAt(lower), b = s.charAt(lower+1);
		if(a == b)//add to the running total and recurr
			return recFindAnswer(s, ++lower, upper) + Integer.parseInt(s.substring(lower, lower + 1));
		else//recurr with no addition
			return recFindAnswer(s, ++lower, upper) + 0;


	}

	public static void main(String[] args)
	{
		Scanner stdin = new Scanner(System.in);
		String num;
		num = stdin.next();
		int i = 0;
		if(num.charAt(0) == num.charAt(num.length() - 1))//to handle cyclical case i.e. last == first
			i += Integer.parseInt(num.substring(0,1));
		System.out.println(recFindAnswer(num, 0, num.length()) + i);
	}
}
