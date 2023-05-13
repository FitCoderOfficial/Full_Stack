export interface User {
    id:                 number;
    videos:             Video[];
    videos_count:       number;
    short_videos:       Video[];
    short_videos_count: number;
    last_login:         Date | null;
    is_superuser:       boolean;
    username:           string;
    first_name:         string;
    last_name:          string;
    is_staff:           boolean;
    is_active:          boolean;
    date_joined:        Date;
    email:              string;
    image:              string;
    bio:                string;
    groups:             any[];
    user_permissions:   any[];
}

export interface Video {
    id:              number;
    uploader:        string;
    uploader_image:  string;
    uploader_id:     number;
    likes:           any[];
    dislikes:        any[];
    short_comments?: Comment[];
    title:           string;
    description:     string;
    upload_date:     Date;
    view_count:      number;
    publish_date:    null;
    video_url:       string;
    thumbnail:       null;
    is_public:       boolean;
    duration:        null;
    category:        null;
    tags:            any[];
    comments?:       Comment[];
}

export interface Comment {
    id:                 number;
    author:             string;
    author_image:       string;
    short_video_title?: string;
    content:            string;
    created_at:         Date;
    updated_at:         Date;
    user:               number;
    short_video?:       number;
    video_title?:       string;
    video?:             number;
}



// redux
export interface AuthState {
    access:string | null;
    refresh: string | null;
    is_authenticated: boolean;
    is_loading: boolean;
    user: User | null;
}


export interface Form {
    [key:string]:string 
}