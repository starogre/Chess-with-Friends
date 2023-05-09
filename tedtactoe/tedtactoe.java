
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;
import java.util.List;

public class TicTacToe {

	static ArrayList<Integer> playerPositions = new ArrayList<Integer>();
	static ArrayList<Integer> tedaiPositions = new ArrayList<Integer>();

	public static void main(String[] args) {
	
		char[] [] gameBoard = {{' ', '|', ' ', '|', ' '},
			{'-', '+', '-', '+', '-'},
			{' ', '|', ' ', '|', ' '},
			{'-', '+', '-', '+', '-'},
			{' ', '|', ' ', '|', ' '}};

		
		printGameBoard(gameBoard);

		while(true) {
			Scanner scan = new Scanner(System.in);
			System.out.println("Enter your GOTDAM placement (1-9):");
			int playerPos = scan.nextInt();
			while(playerPositions.contains(playerPos) || tedaiPositions.contains(playerPos)) {
				System.out.println("Greg P awakens from his slumber, RE-ENTER MOVE - he exclaims");
				playerPos = scan.nextInt();
			}

			placePiece(gameBoard, playerPos, "player");

			String result = checkVinner();
			if(result.length() > 0) {
				System.out.println(result);
				break;
			}
		
			Random rand = new Random();
			int tedaiPos = rand.nextInt(9) + 1;
			while(playerPositions.contains(tedaiPos) || tedaiPositions.contains(tedaiPos)) {
				tedaiPos = rand.nextInt(9) + 1;
			}

			placePiece(gameBoard, tedaiPos, "TedAI");

			printGameBoard(gameBoard);

			result = checkVinner();
			if(result.length() > 0) {
				System.out.println(result);
				break;

			}
		}
					
	}	
		

	public static void printGameBoard(char [][] gameBoard) {
		for(char [] row : gameBoard) {
			for (char c : row) {
				System.out.print(c);
		}
		System.out.println();

		}
	}

	public static void placePiece(char[][] gameBoard, int pos, String user) {

		char symbol = ' ';

		if(user.equals("player")){
			symbol = 'X';
			playerPositions.add(pos);
		} else if(user.equals("TedAI")) {
			symbol = '0';
			tedaiPositions.add(pos);
		}

		switch(pos) {
			case 1:
				gameBoard[0][0] = symbol;
				break;
			case 2:
				gameBoard[0][2] = symbol;
				break;
			case 3:
				gameBoard[0][4] = symbol;
				break;
			case 4:
				gameBoard[2][0] = symbol;
				break;
			case 5:
				gameBoard[2][2] = symbol;
				break;
			case 6:
				gameBoard[2][4] = symbol;
				break;
			case 7:
				gameBoard[4][0] = symbol;
				break;
			case 8:
				gameBoard[4][2] = symbol;
				break;
			case 9:
				gameBoard[4][4] = symbol;
				break;
			default:
				break;

		}
	}

	public static String checkVinner() {
	
		List topRow = Arrays.asList(1, 2, 3);
		List midRow = Arrays.asList(4, 5, 6);
		List botRow = Arrays.asList(7, 8, 9);
		List leftCol = Arrays.asList(1, 4, 7);
		List midCol = Arrays.asList(2, 5, 8);
		List rightCol = Arrays.asList(3, 6, 9);
		List cross1 = Arrays.asList(1, 5, 9);
		List cross2 = Arrays.asList(7, 5, 3);

		List<List> vinning = new ArrayList<List>();
		vinning.add(topRow);
		vinning.add(midRow);
		vinning.add(botRow);
		vinning.add(leftCol);
		vinning.add(midCol);
		vinning.add(rightCol);
		vinning.add(cross1);
		vinning.add(cross2);
		
		for(List l : vinning) {
			if(playerPositions.containsAll(l)){
				return "TedAI Slain";
			} else if(tedaiPositions.containsAll(l)) {
				return "Slain by TedAI";
			} else if(playerPositions.size() + tedaiPositions.size() == 9){
				return "GREG SIGINT";
			
			}
		}

		return "";
	}
}
