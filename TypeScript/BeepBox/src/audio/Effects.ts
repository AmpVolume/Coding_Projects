export class Effects {


    context:AudioContext;



    constructor(
        context:AudioContext
    ){

        this.context=context;

    }





    createDelay(
        time:number = 0.25
    ){


        const delay =
        this.context.createDelay();


        delay.delayTime.value =
            time;



        return delay;

    }





    createFilter(){

        const filter =
        this.context.createBiquadFilter();



        filter.type="lowpass";


        filter.frequency.value=1000;



        return filter;

    }



}