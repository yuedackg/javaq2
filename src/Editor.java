
public class Editor {
	private GapBuffer buf;
	private int cursor = 0;
	
	private Editor( String text) {
		buf = new GapBuffer( text);
	}
	private void run() {

		//	Dispalay.output( buf, cursor);
		char ch;
		while((ch=CharReader.get()) != CharReader.EOF) {
			switch( ch) {
			case CharReader.MOVE_FORWARD:
				moveCursor( 1);
				break;
			case CharReader.MOVE_BACKWARD:
				moveCursor( -1);
				break;
			case CharReader.DELETE:
				if ( cursor <buf.length()) {
					buf.delete();
				}
			default:
				buf.insert(,ch);
				break;
			}
			//	Display.output( buf,cursor);
			
		}
	}
	private void moveCursor(int n) {
		// TODO Auto-generated method stub
		
	}
}

class CharReader{
	public static final char EOF = 0;
	static final int MOVE_FORWARD = 1;
	static final int MOVE_BACKWARD = 2;
	static final int DELETE = 3;
	static final int INSERT = 3;
	public static   char get() {
		return 0;
		
	}
	public void delete() {
		
	}
	
}