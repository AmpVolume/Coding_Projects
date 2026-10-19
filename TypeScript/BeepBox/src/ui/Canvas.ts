export class Canvas {


    element:HTMLCanvasElement;


    context:CanvasRenderingContext2D;



    constructor(
        width:number = 800,
        height:number = 400
    ){


        this.element =
        document.createElement(
            "canvas"
        );


        this.element.width =
        width;


        this.element.height =
        height;



        this.context =
        this.element.getContext(
            "2d"
        )!;


    }





    clear(){

        this.context.clearRect(
            0,
            0,
            this.element.width,
            this.element.height
        );

    }





    drawGrid(){

        const ctx =
        this.context;


        for(
            let x=0;
            x<this.element.width;
            x+=50
        ){

            ctx.beginPath();

            ctx.moveTo(
                x,
                0
            );

            ctx.lineTo(
                x,
                this.element.height
            );

            ctx.stroke();

        }


    }





    mount(
        parent:HTMLElement
    ){

        parent.appendChild(
            this.element
        );

    }



}