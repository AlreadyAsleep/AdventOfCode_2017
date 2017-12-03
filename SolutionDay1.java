import java.util.*;
public class SolutionDay1
{
	public static int recFindAnswer(String s, int lower, int upper)
	{
		
		if(lower == upper - 1)
			return 0;
		char a = s.charAt(lower), b = s.charAt(lower+1);
		if(a == b)
			return recFindAnswer(s, ++lower, upper) + Integer.parseInt(s.substring(lower, lower + 1));
		else
			return recFindAnswer(s, ++lower, upper) + 0;


	}

	public static void main(String[] args)
	{
		Scanner stdin = new Scanner(System.in);
		String num;
		num = stdin.next();
		int i = 0;
		if(num.charAt(0) == num.charAt(num.length() - 1))
			i += Integer.parseInt(num.substring(0,1));
		System.out.println(recFindAnswer(num, 0, num.length()) + i);
	}
}