import { Song } from "./model/Song";
import { Channel } from "./model/Channel";
import { Pattern } from "./model/Pattern";
import { Note } from "./model/Note";
import { Instrument } from "./model/Instrument";

import { AudioEngine } from "./audio/AudioEngine";

import { PlaybackController } from "./playback/PlaybackController";

import { SongDocument } from "./editor/SongDocument";
import { SongEditor } from "./editor/SongEditor";
import { Transport } from "./editor/Transport";

import { Toolbar } from "./editor/Toolbar";

import { Button } from "./ui/Button";
import { Window } from "./ui/Window";



// =================================
// CREATE SONG
// =================================


const song =
new Song(
    "song01",
    "Untitled Song"
);



// =================================
// CREATE INSTRUMENT
// =================================


const synth =
new Instrument(
    "instrument01",
    "Basic Synth"
);

synth.waveform = "sawtooth";




// =================================
// CREATE CHANNEL
// =================================


const channel =
new Channel(
    "channel01",
    "Lead Synth",
    synth
);


song.addChannel(
    channel
);




// =================================
// CREATE PATTERN
// =================================


const pattern =
new Pattern(
    "pattern01",
    "Melody",
    4
);


channel.addPattern(
    pattern
);




// =================================
// ADD NOTES
// =================================


pattern.addNote(
    new Note(
        "note01",
        60,
        0,
        0.5
    )
);


pattern.addNote(
    new Note(
        "note02",
        64,
        1,
        0.5
    )
);


pattern.addNote(
    new Note(
        "note03",
        67,
        2,
        0.5
    )
);


pattern.addNote(
    new Note(
        "note04",
        72,
        3,
        0.5
    )
);





// =================================
// AUDIO ENGINE
// =================================


const audio =
new AudioEngine();






// =================================
// PLAYBACK
// =================================


const playback =
new PlaybackController(
    song,
    audio
);






// =================================
// EDITOR
// =================================


const document =
new SongDocument(
    song
);


const editor =
new SongEditor(
    document
);






// =================================
// TRANSPORT
// =================================


const transport =
new Transport(
    playback
);






// =================================
// TOOLBAR
// =================================


const toolbar =
new Toolbar();






// =================================
// CREATE UI
// =================================


const app =
new Window(
    "UltraBox"
);



const playButton =
new Button(
    "▶ Play"
);



playButton.onClick(
    ()=>{


        console.log(
            "Starting playback..."
        );


        transport.play();


    }
);



const stopButton =
new Button(
    "■ Stop"
);



stopButton.onClick(
    ()=>{


        console.log(
            "Stopping..."
        );


        transport.stop();


    }
);




playButton.mount(
    app.element
);


stopButton.mount(
    app.element
);



app.mount(
    document.body
);






// =================================
// DEBUG
// =================================


console.log(
    "UltraBox Started"
);


console.log(
    song
);





// =================================
// KEYBOARD CONTROLS
// =================================


window.addEventListener(
    "keydown",
    (event)=>{


        if(event.code==="Space")
        {

            transport.play();

        }



        if(event.code==="Escape")
        {

            transport.stop();

        }



    }
);