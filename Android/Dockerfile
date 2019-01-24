FROM openjdk:8-jdk

RUN cd /etc/apt/ &&\
mv sources.list sources_backup.list &&\
echo "\n# 163 sources\n\n\
deb http://mirrors.163.com/debian/ stretch main non-free contrib\n\
deb http://mirrors.163.com/debian/ stretch-updates main non-free contrib\n\
deb http://mirrors.163.com/debian/ stretch-backports main non-free contrib\n\
deb-src http://mirrors.163.com/debian/ stretch main non-free contrib\n\
deb-src http://mirrors.163.com/debian/ stretch-updates main non-free contrib\n\
deb-src http://mirrors.163.com/debian/ stretch-backports main non-free contrib\n\
deb http://mirrors.163.com/debian-security/ stretch/updates main non-free contrib\n\
deb-src http://mirrors.163.com/debian-security/ stretch/updates main non-free contrib"\
>> sources.list

ENV GRADLE_HOME /opt/gradle
ENV GRADLE_VERSION 4.4

RUN set -o errexit -o nounset \
    && echo "Downloading Gradle" \
    && wget --no-verbose --output-document=gradle.zip "https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" \
    && echo "Installing Gradle" \
    && unzip gradle.zip \
    && rm gradle.zip \
    && mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" \
    && ln --symbolic "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle

ENV ANDROID_HOME /opt/android-sdk

ARG ANDROID_SDK_VERSION=4333796
RUN mkdir -p $ANDROID_HOME \
    && cd $ANDROID_HOME \
    && wget -q https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_VERSION}.zip \
    && unzip *tools*linux*.zip \
    && rm *tools*linux*.zip

ENV PATH ${PATH}:${ANDROID_HOME}/tools/bin

RUN yes | sdkmanager "platform-tools"
