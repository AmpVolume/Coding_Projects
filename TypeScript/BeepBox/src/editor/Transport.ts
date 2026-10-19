import { PlaybackController } from "../playback/PlaybackController";


export class Transport {



    playback:PlaybackController;



    constructor(
        playback:PlaybackController
    ){

        this.playback=playback;

    }





    play(){

        this.playback.play();

    }





    pause(){

        this.playback.pause();

    }





    stop(){

        this.playback.stop();

    }



}