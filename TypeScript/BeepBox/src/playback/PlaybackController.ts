import { Song } from "../model/Song";
import { AudioEngine } from "../audio/AudioEngine";

import { Clock } from "./Clock";
import { PlaybackCursor } from "./PlaybackCursor";
import { Scheduler } from "./Scheduler";



export class PlaybackController {



    song:Song;


    audio:AudioEngine;


    clock:Clock;


    cursor:PlaybackCursor;


    scheduler:Scheduler;



    interval:any;




    constructor(
        song:Song,
        audio:AudioEngine
    ){


        this.song=song;

        this.audio=audio;



        this.clock =
        new Clock(
            song.timeline.bpm
        );



        this.cursor =
        new PlaybackCursor();



        this.scheduler =
        new Scheduler(
            song,
            audio,
            this.cursor
        );


    }






    play(){


        if(
            this.cursor.playing
        )
            return;



        this.cursor.playing=true;



        this.clock.start();



        this.interval =
        setInterval(()=>{


            this.cursor.beat =
            this.clock.getBeat();



            this.scheduler.update();



        },50);



    }







    pause(){


        this.cursor.playing=false;



        this.clock.stop();



        clearInterval(
            this.interval
        );


    }







    stop(){


        this.pause();



        this.cursor.reset();


    }




}