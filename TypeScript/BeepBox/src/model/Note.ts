export class Note {
    id: string;

    pitch: number;        // MIDI pitch (60 = C4)
    velocity: number;     // 0-1 volume
    start: number;        // beat position
    duration: number;     // length in beats

    constructor(
        id: string,
        pitch: number,
        start: number,
        duration: number,
        velocity: number = 1
    ) {
        this.id = id;
        this.pitch = pitch;
        this.start = start;
        this.duration = duration;
        this.velocity = velocity;
    }


    getEndTime(): number {
        return this.start + this.duration;
    }


    clone(): Note {
        return new Note(
            this.id,
            this.pitch,
            this.start,
            this.duration,
            this.velocity
        );
    }
}