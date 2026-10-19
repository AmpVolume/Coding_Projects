export class Theme {


    background:string;

    panel:string;

    text:string;

    accent:string;



    constructor(){

        this.background = "#111111";

        this.panel = "#222222";

        this.text = "#ffffff";

        this.accent = "#00ff88";

    }





    apply(
        element:HTMLElement
    ){

        element.style.background =
        this.background;

        element.style.color =
        this.text;

    }



}