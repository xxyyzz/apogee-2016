function chessinit(){
	chess.init();
}
var chess={
	Bishop: function(color,index){
		var obj = new Object();
		var html= document.createElement("div");
		html.setAttribute("class","bishop");
		html.setAttribute("color",color);
		html.setAttribute("index",index);
		html.style.backgroundImage = "url('/2016/static/lacuna/img/puzzle/"+color+".svg')";	 
		$(html).draggable({ 
			revert: true,
			helper: 'clone',
			opacity: 0.5 
		});
		obj.html=html;
		obj.color = color;
		obj.getOpponents = function(){
			if(this.color==0){
				return chess.bishops[1];
			}
			return chess.bishops[0];
		}
		obj.isValidMove =function(box){
			var diffX,diffY,m;
			diffX= box.x-this.box.x;
			diffY=box.y-this.box.y;
			m=diffX/diffY;
			if(m==1 || m==-1){
				return 1;
			}
			return 0;
		}
		obj.isSafeMove= function(box){
			for(var i=0;i<2;i++){
				if(this.getOpponents()[i].isValidMove(box)){
					return 0;
				}
			}
			return 1;
		}
		obj.makeMove= function(box){
			var h= (0.75*window.innerHeight);
			if(this.isSafeMove(box) && this.isValidMove(box) && !box.occupied){
				this.box.occupied =false;
				this.box = box;
				this.box.occupied=true;
				this.html.style.top = (this.box.x*(h*0.25));
				this.html.style.left = (this.box.y*(h*0.25));
				return 1;
			}
			return 0;
		}

		return obj;
	},
	Box: function(x,y){
		var obj = new Object();
		var html= document.createElement("div");
		html.setAttribute("class","chess-box");
		html.setAttribute("x",x);
		html.setAttribute("y",y);
		if((x+y)%2==0){
			html.style.backgroundImage="url('/2016/static/lacuna/img/puzzle/black_check.png')";
		}else{
			html.style.backgroundImage="url('/2016/static/lacuna/img/puzzle/white_check.png')";
		}
		$(html).droppable({
  			accept: '.bishop',
			drop: function(event, ui) {
				var bishop = chess.bishops[ui.draggable.attr("color")][ui.draggable.attr("index")];
  				var box = chess.boxs[$(this).attr("x")][$(this).attr("y")];
				if(bishop.makeMove(box) == 1) {
					$('.ui-draggable-dragging').hide();
					chess.checkForVictory();
				}
			} 
		});
		obj.x= x;
		obj.occupied =false;
		obj.y= y;
		obj.html= html;
		return obj;
	},
	createBoxs: function(){
		var board= document.getElementById("chess-board");
		for(var i=0;i<4;i++){
			for(var j=0;j<5;j++){
				this.boxs[i][j] = this.Box(i,j);
				board.appendChild(this.boxs[i][j].html);
			}
		}
	},
	createBishops: function(){
		var board= document.getElementById("chess-board");
		for(var i=0;i<2;i++){
			this.bishops[0][i] = this.Bishop(0,i);
			this.bishops[1][i] = this.Bishop(1,i);
			this.bishops[0][i].box=this.boxs[(2*i)+1][0];
			this.bishops[1][i].box=this.boxs[(2*i)+1][4];
			this.bishops[0][i].box.occupied=true;
			this.bishops[1][i].box.occupied=true;
			board.appendChild(this.bishops[1][i].html);
			board.appendChild(this.bishops[0][i].html);
		}
	},
	checkForVictory: function(){
		 for(var i=0;i<2;i++){
		 	if(!((this.bishops[0][i].box==this.boxs[3][4] || this.bishops[0][i].box==this.boxs[1][4]) && (this.bishops[1][i].box==this.boxs[1][0] || this.bishops[1][i].box==this.boxs[3][0]))){
		 		return 0;
		 	}
		}
		window.alert("You won!");
		return 1;
	},
	setStyle : function(){
		var h= (0.75*window.innerHeight);
		var chessBoard= document.getElementById("chess-board");
		var chessBoxs= document.getElementsByClassName("chess-box");
		chessBoard.style.height= h;
		chessBoard.style.width= (h*1.25);
		for(var i=0; i<chessBoxs.length;i++){
			chessBoxs[i].style.height=(h*0.25);
			chessBoxs[i].style.width=(h*0.25);
		};
		for(var i=0; i<2;i++){
			for(var j=0;j<2;j++){
				this.bishops[i][j].html.style.height=(h*0.25);
				this.bishops[i][j].html.style.width=(h*0.25);
				this.bishops[i][j].html.style.top = (this.bishops[i][j].box.x*(h*0.25));
				this.bishops[i][j].html.style.left = (this.bishops[i][j].box.y*(h*0.25));
			}
		}
	},
	initArrays: function(){
		this.boxs= new Array(5);
		for(var i=0; i<5;i++){
			this.boxs[i]= new Array(4);
		};
		this.bishops= new Array(2);
		for(var i=0; i<2;i++){
			this.bishops[i]= new Array(2);
		};
	},
	init: function(){
		this.initArrays();
		this.createBoxs();
		this.createBishops();
		this.setStyle();
	}
}