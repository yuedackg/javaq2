
public class GapBuffer {
	private static final int INITIAL_GAP_SIZE = 128;
	private char[] buffer;
	private int gapOffset = 0;
	private int gapSize = INITIAL_GAP_SIZE;
	
	GapBuffer(String initialText) {
		buffer = new char[ initialText.length() + gapSize];
		System.arraycopy(initialText.toCharArray(), 0, buffer, gapSize, initialText.length());
		
	}
	
	void insert( int offset, char ch) {
		confirmGap( offset);
		buffer[gapOffset++]=ch;
		
	}
	void delete( int offset) {
		
	}
	char charAt( int offset) {
		
	}
	int length( ) {
		return 	;
	
	}
	private void confirmGap( int newGapOffset) {
		
	}
}
