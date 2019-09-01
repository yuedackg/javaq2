
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
		if(length() == 0)
			return ;
		confirmGap( offset + 1);
		gapOffset--;
		gapSize++;
	}
	char charAt( int offset) {
		if(offset >= gapOffset)
			offset += ;
		return buffer[offset];
	}
	int length( ) {
		return 	buffer.length;
	
	}
	private void confirmGap( int newGapOffset) {
		
	}
}
