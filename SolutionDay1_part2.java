import java.util.*;
public class SolutionDay1_part2
{
	public static int FindAnswer(String s)
	{
		int half = s.length() / 2;//index of the halfway point
		int count = 0;
		for(int i = 0;  i < half; i++)
		{
			if(s.charAt(i) == s.charAt(i + half))
			{
				System.out.println(s.substring(i, i+1));
				count += 2 * Integer.parseInt(s.substring(i, i+1));// because each occurence counts twice
			}
		}

		if(s.charAt(half) == s.charAt(s.length() - 1))//finally check the char at the halfway point against the last char
			count += Integer.parseInt(s.substring(half, half+1)); 
		return count;
	}

	public static void main(String[] args)
	{
		Scanner stdin = new Scanner(System.in);
		String num;
		num = stdin.next();
		System.out.println(FindAnswer(num));
	}
}
