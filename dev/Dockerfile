FROM ubuntu:latest

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    curl \
    wget \
    git \
    vim \
    ninja-build \
    gettext \
    libtool \
    libtool-bin \
    autoconf \
    automake \
    cmake \
    g++ \
    pkg-config \
    unzip \
    build-essential \
    python3 \
    python3-pip \
    zsh \
    tree \
    openjdk-19-jdk

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install pytest

RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" || true

RUN git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

RUN sed -i 's/plugins=(git)/plugins=(git zsh-autosuggestions)/' ~/.zshrc

RUN echo "set number\n\
set hlsearch\n\
set mouse=a\n\
set noerrorbells\n\
set novisualbell\n\
set autoindent\n\
set softtabstop=4\n\
set tabstop=4\n\
set shiftwidth=4\n\
set expandtab\n\
syntax enable" > ~/.vimrc

WORKDIR /neovim
RUN git clone https://github.com/neovim/neovim . && \
    git checkout stable && \
    make CMAKE_BUILD_TYPE=RelWithDebInfo && \
    make install

WORKDIR /app
COPY . /app

RUN mkdir -p /root/.config/nvim

COPY init.lua /root/.config/nvim/init.lua

CMD ["/usr/bin/zsh"]
