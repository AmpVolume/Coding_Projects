export class Mixer {


    context:AudioContext;


    master:GainNode;



    constructor(
        context:AudioContext
    ){

        this.context=context;


        this.master =
        context.createGain();



        this.master.gain.value=1;


        this.master.connect(
            context.destination
        );

    }



    createChannel(){

        const channel =
        this.context.createGain();


        channel.connect(
            this.master
        );


        return channel;

    }




    setMasterVolume(
        value:number
    ){

        this.master.gain.value=value;

    }



}